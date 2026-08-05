import csv
import shutil
from pathlib import Path
import statistics
import cv2

base = Path(r"d:\Dataset\OneDrive\Documents\Projects\Road-Vision-Nepal\phase2_hybrid_segmentation\dataset")
src_dir = base / 'extracted_frames' / 'v04_review'
out_dir = base / 'extracted_frames' / 'v04_calibration'
out_dir.mkdir(parents=True, exist_ok=True)
for p in out_dir.glob('*'):
    if p.is_file():
        p.unlink()

files = sorted([p for p in src_dir.glob('v04_frame_*.jpg') if p.is_file()])
if not files:
    raise SystemExit('No source frames found')

records = []
for path in files:
    img = cv2.imread(str(path), cv2.IMREAD_GRAYSCALE)
    if img is None:
        continue
    lap = cv2.Laplacian(img, cv2.CV_64F)
    score = float(lap.var())
    records.append((score, path.name))

records.sort(key=lambda x: x[0])

n = len(records)
# 5 equal-sized bins by sorted score; bin 1 = blurriest, bin 5 = sharpest
bin_boundaries = []
for i in range(6):
    bin_boundaries.append(int(round(i * n / 5)))
# Ensure valid, monotonic boundaries
bin_boundaries[0] = 0
bin_boundaries[-1] = n
for i in range(1, len(bin_boundaries) - 1):
    if bin_boundaries[i] >= bin_boundaries[i + 1]:
        bin_boundaries[i] = bin_boundaries[i + 1] - 1


def assign_bin(index: int) -> int:
    if index < bin_boundaries[1]:
        return 1
    if index < bin_boundaries[2]:
        return 2
    if index < bin_boundaries[3]:
        return 3
    if index < bin_boundaries[4]:
        return 4
    return 5

records_with_bin = []
for index, (score, name) in enumerate(records):
    records_with_bin.append((score, name, assign_bin(index)))

selected = []
for bin_number in range(1, 6):
    bin_records = [r for r in records_with_bin if r[2] == bin_number]
    if not bin_records:
        continue
    if len(bin_records) >= 4:
        idxs = [int(round(j * (len(bin_records) - 1) / 3)) for j in range(4)]
    else:
        idxs = list(range(len(bin_records)))
    for idx in idxs:
        selected.append(bin_records[idx])

if len(selected) < 20:
    for item in records_with_bin:
        if item not in selected:
            selected.append(item)
        if len(selected) >= 20:
            break

selected = selected[:20]

log_path = base / 'extracted_frames' / 'v04_calibration_log.csv'
with log_path.open('w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['original_filename', 'blur_score', 'bin_number'])
    for score, name, bin_number in selected:
        stem = Path(name).stem
        score_str = f'{score:.3f}'.replace('.', '_')
        out_name = f'{score_str}_{stem}.jpg'
        shutil.copy2(src_dir / name, out_dir / out_name)
        writer.writerow([name, f'{score:.6f}', bin_number])

scores_only = [score for score, _, _ in records_with_bin]
print('SUMMARY')
print(f'min={min(scores_only):.6f}')
print(f'max={max(scores_only):.6f}')
print(f'median={statistics.median(scores_only):.6f}')
for bin_number in range(1, 6):
    bin_scores = [score for score, _, b in records_with_bin if b == bin_number]
    if bin_scores:
        print(f'bin_{bin_number}_range=[{min(bin_scores):.6f}, {max(bin_scores):.6f}]')

print(f'copied_files={len(selected)}')
print(f'output_dir={out_dir}')
print(f'log_csv={log_path}')

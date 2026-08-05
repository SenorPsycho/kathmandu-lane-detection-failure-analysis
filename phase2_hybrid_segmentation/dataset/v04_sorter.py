"""
v04_sorter.py — Fast keyboard-driven binary sort for Video 4 frames
Requires: opencv-python (pip install opencv-python --break-system-packages if missing)

Controls:
  1 -> Tier 1 (clean)      -> moves to v04_clean/
  2 -> Tier 2 (stress)     -> moves to v04_stress/
  u -> undo last move, re-show it
  q -> quit (progress is saved automatically since files are moved, not copied)

Optional:
  --auto-only --threshold 530.0
    Automatically moves every frame with blur score >= threshold into v04_clean/
    and exits without launching the interactive UI.
"""

import argparse
import os
import shutil
import cv2

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, "extracted_frames", "v04_review")
CLEAN_DIR = os.path.join(BASE_DIR, "extracted_frames", "v04_clean")
STRESS_DIR = os.path.join(BASE_DIR, "extracted_frames", "v04_stress")

os.makedirs(CLEAN_DIR, exist_ok=True)
os.makedirs(STRESS_DIR, exist_ok=True)


def list_frames(directory):
    return sorted([f for f in os.listdir(directory) if f.lower().endswith((".jpg", ".png", ".jpeg"))])


def compute_blur_score(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        return None
    lap = cv2.Laplacian(img, cv2.CV_64F)
    return float(lap.var())


def auto_sort_by_score(threshold):
    frames = list_frames(SRC_DIR)
    moved = 0
    remaining = []

    for fname in frames:
        path = os.path.join(SRC_DIR, fname)
        score = compute_blur_score(path)
        if score is None:
            continue
        if score >= threshold:
            dest = os.path.join(CLEAN_DIR, fname)
            shutil.move(path, dest)
            moved += 1
        else:
            remaining.append(fname)

    return moved, remaining


def run_interactive_sort(frames):
    history = []
    WINDOW = "v04 sorter  |  1=clean  2=stress  u=undo  q=quit"
    cv2.namedWindow(WINDOW, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(WINDOW, 1280, 720)

    i = 0
    total = len(frames)
    while i < total:
        fname = frames[i]
        path = os.path.join(SRC_DIR, fname)
        img = cv2.imread(path)
        if img is None:
            i += 1
            continue

        display = img.copy()
        label = f"{i+1}/{total}  {fname}"
        cv2.putText(display, label, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow(WINDOW, display)

        key = cv2.waitKey(0) & 0xFF

        if key == ord('1'):
            dest = os.path.join(CLEAN_DIR, fname)
            shutil.move(path, dest)
            history.append((path, dest))
            i += 1
        elif key == ord('2'):
            dest = os.path.join(STRESS_DIR, fname)
            shutil.move(path, dest)
            history.append((path, dest))
            i += 1
        elif key == ord('u'):
            if history:
                last_src, last_dest = history.pop()
                shutil.move(last_dest, last_src)
                i -= 1
        elif key == ord('q'):
            break

    cv2.destroyAllWindows()
    print(f"Done. Reviewed {i}/{total} frames this session.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--auto-only", action="store_true", help="Auto-sort frames above the blur threshold and exit")
    parser.add_argument("--threshold", type=float, default=530.0, help="Blur-score threshold for clean auto-sort")
    args = parser.parse_args()

    moved, remaining = auto_sort_by_score(args.threshold)
    print(f"Auto-sorted {moved} frames to clean using threshold {args.threshold:.3f}")
    print(f"Remaining in review: {len(remaining)}")

    if args.auto_only:
        print(f"Clean: {len(os.listdir(CLEAN_DIR))} | Stress: {len(os.listdir(STRESS_DIR))} | Remaining in {SRC_DIR}: {len(remaining)}")
    else:
        run_interactive_sort(remaining)
        print(f"Clean: {len(os.listdir(CLEAN_DIR))} | Stress: {len(os.listdir(STRESS_DIR))} | Remaining in {SRC_DIR}: {len(os.listdir(SRC_DIR))}")

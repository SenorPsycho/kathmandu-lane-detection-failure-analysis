#!/usr/bin/env python3
"""
Extract frames by blur score bands.
Categorizes and copies frames into folders based on blur severity.
"""

import os
import csv
import shutil
from pathlib import Path

# Configuration
BLUR_CSV = r"D:\Dataset\OneDrive\Documents\Projects\Road-Vision-Nepal\phase2_hybrid_segmentation\dataset\v04_blur_scores.csv"
SOURCE_DIR = r"D:\Dataset\OneDrive\Documents\Projects\Road-Vision-Nepal\phase2_hybrid_segmentation\dataset\extracted_frames\v04_review"
BASE_TARGET_DIR = r"D:\Dataset\OneDrive\Documents\Projects\Road-Vision-Nepal\phase2_hybrid_segmentation\dataset\extracted_frames"

# Define bands
BANDS = {
    'under50': (0, 50),
    '50to150': (50, 150),
    '150to400': (150, 400),
    'over400': (400, float('inf'))
}

def main():
    # Create output folders for extractable bands
    for band_name in ['under50', '50to150']:
        band_dir = os.path.join(BASE_TARGET_DIR, f'v04_blur_{band_name}')
        os.makedirs(band_dir, exist_ok=True)
        print(f"✓ Created: {band_dir}")
    
    # Read CSV and categorize
    band_counts = {name: 0 for name in BANDS.keys()}
    frame_data = {name: [] for name in BANDS.keys()}
    
    print(f"\nReading blur scores from: {BLUR_CSV}")
    with open(BLUR_CSV, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            filename = row['filename']
            score = float(row['blur_score'])
            
            # Categorize
            for band_name, (min_score, max_score) in BANDS.items():
                if min_score <= score < max_score:
                    band_counts[band_name] += 1
                    frame_data[band_name].append((filename, score))
                    break
    
    # Copy frames for extractable bands
    print("\nCopying frames by blur band:")
    for band_name in ['under50', '50to150']:
        target_dir = os.path.join(BASE_TARGET_DIR, f'v04_blur_{band_name}')
        frames = frame_data[band_name]
        
        for filename, score in frames:
            src = os.path.join(SOURCE_DIR, filename)
            dst = os.path.join(target_dir, filename)
            try:
                shutil.copy2(src, dst)
            except Exception as e:
                print(f"  ✗ Error copying {filename}: {e}")
        
        print(f"  ✓ {band_name}: {len(frames)} frames copied")
    
    # Report summary
    print("\n" + "="*60)
    print("BLUR BAND SUMMARY")
    print("="*60)
    print(f"Under 50:        {band_counts['under50']:4d} frames  [SEVERE blur]")
    print(f"50–150:          {band_counts['50to150']:4d} frames  [Heavy blur]")
    print(f"150–400:         {band_counts['150to400']:4d} frames  [Moderate blur]")
    print(f"Over 400:        {band_counts['over400']:4d} frames  [Sharp images]")
    print(f"{'─'*40}")
    print(f"TOTAL:           {sum(band_counts.values()):4d} frames")
    print("="*60)
    
    # Extracted vs. not extracted
    print(f"\nFolders created with copies:")
    print(f"  • v04_blur_under50/   ({band_counts['under50']} frames)")
    print(f"  • v04_blur_50to150/   ({band_counts['50to150']} frames)")
    print(f"\nNot extracted (report only):")
    print(f"  • 150–400 band:       {band_counts['150to400']} frames")
    print(f"  • Over 400 band:      {band_counts['over400']} frames")

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Blur detection script using variance of Laplacian.
Scans all frames in v04_review/ and outputs sharpness scores to CSV.
"""

import os
import cv2
import csv
from pathlib import Path

# Configuration
INPUT_FOLDER = r"D:\Dataset\OneDrive\Documents\Projects\Road-Vision-Nepal\phase2_hybrid_segmentation\dataset\extracted_frames\v04_review"
OUTPUT_CSV = r"D:\Dataset\OneDrive\Documents\Projects\Road-Vision-Nepal\phase2_hybrid_segmentation\dataset\v04_blur_scores.csv"

def compute_blur_score(image_path):
    """
    Compute blur score using variance of Laplacian.
    Higher score = sharper image, lower score = blurrier image.
    """
    img = cv2.imread(image_path)
    if img is None:
        return None
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()
    return laplacian_var

def main():
    print(f"Scanning frames in: {INPUT_FOLDER}")
    
    results = []
    frame_files = sorted([f for f in os.listdir(INPUT_FOLDER) if f.endswith('.jpg')])
    total_frames = len(frame_files)
    
    print(f"Found {total_frames} frames to process...")
    
    for idx, filename in enumerate(frame_files, 1):
        filepath = os.path.join(INPUT_FOLDER, filename)
        blur_score = compute_blur_score(filepath)
        
        if blur_score is not None:
            results.append({
                'filename': filename,
                'blur_score': blur_score
            })
            
            if idx % 100 == 0:
                print(f"  Processed {idx}/{total_frames}...")
    
    # Sort by blur_score (ascending = blurriest first)
    results.sort(key=lambda x: x['blur_score'])
    
    # Write CSV
    print(f"\nWriting results to: {OUTPUT_CSV}")
    with open(OUTPUT_CSV, 'w', newline='') as csvfile:
        fieldnames = ['filename', 'blur_score']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(results)
    
    print(f"✓ Blur detection complete!")
    print(f"  Total frames processed: {len(results)}")
    print(f"  Blurriest frame: {results[0]['filename']} (score: {results[0]['blur_score']:.2f})")
    print(f"  Sharpest frame: {results[-1]['filename']} (score: {results[-1]['blur_score']:.2f})")
    print(f"  Results saved to: v04_blur_scores.csv")

if __name__ == '__main__':
    main()
    
    


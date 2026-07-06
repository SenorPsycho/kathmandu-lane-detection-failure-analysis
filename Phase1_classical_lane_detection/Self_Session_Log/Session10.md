# RoadVision Nepal Research Log

## Session 10 June 20, Friday

### What I learned

**HSV color space basics for lane detection**
- HSV separates color information (hue) from brightness (value), which is more natural for detecting colored objects than BGR
- Yellow lane markings occupy a specific hue range, and white occupies a different range
- By creating masks for just yellow and white, we can eliminate everything else before Canny even runs
- This is pre-filtering rather than post-filtering: remove non-road-colors first, then run the classical pipeline on the filtered result
- The tradeoff is that this approach only works when markings have consistent colors; on uncolored or unmarked roads it becomes useless

**Mask creation with cv.inRange and combining masks**
- cv.inRange creates a binary mask where pixels inside the HSV range become white and everything outside becomes black
- Two separate masks can be combined with cv.bitwise_or to create a union, keeping all pixels that matched either color
- cv.bitwise_and applies the combined mask to the original BGR frame, keeping only the colored regions

**Tuning HSV ranges through observation**
- Starting ranges rarely work perfectly; you have to watch the output and adjust
- Yellow range started at H 20-30 but needed to expand to H 15-35 to catch all yellow lane marking pixels
- Saturation threshold for yellow was lowered to 120 to reject yellow vegetation and noise, keeping only strong yellows
- White range is trickier because it occupies multiple hue bands but all have very low saturation and high value
- White range settled at lower [0, 0, 200] and upper [179, 50, 255], capturing any hue with nearly zero saturation and high brightness

**The vanishing point and line length problem**
- Setting y2 too high (like at y1*0.6) means lines extend all the way to the horizon and can cross there visually
- Moving y2 further down (to y1*0.75) means lines stop in the middle of the frame where perspective hasn't converged them yet
- This is a drawing choice, not a detection issue, but it makes the output look much more natural and lane-like

### What I built
- Added hsv_filter() function that converts BGR to HSV, creates yellow and white masks separately, combines them with bitwise_or, and applies to the original frame with bitwise_and
- Integrated the HSV filter into the main loop as the very first step after frame capture, before grayscale conversion
- Modified make_line() to place y2 at y1*0.75 instead of y1*0.6, stopping lines in the middle of frame rather than extending to vanishing point
- Both videos running with the HSV pre-processing step in place before all other stages

### HSV ranges used

Yellow mask: lower bound [15, 120, 80], upper bound [35, 255, 255]
- Hue 15-35 covers the yellow spectrum
- Saturation 120 rejects pale yellows and vegetation
- Value 80-255 captures all brightness levels

White mask: lower bound [0, 0, 200], upper bound [179, 50, 255]
- Hue 0-179 accepts any hue because white is hue-independent
- Saturation 0-50 captures only near-grayscale colors
- Value 200-255 captures only bright whites, rejecting gray road surface

### Observations on HSV filtered Highway
- The yellow left lane marking was isolated perfectly, appearing as a clean yellow region on black background
- The white dashed right lane was partially preserved in some frames where dashes existed
- After filtering, the grayscale conversion had much cleaner input with non-road colors already removed
- The Hough line detection found the left yellow line consistently and reliably tracked it frame to frame
- The right white line detection flickered during dash gaps, same as before but with less noise interference
- Lines converged naturally toward the horizon and no longer crossed in the middle of the frame
- The overall output was cleaner and more stable than the baseline pipeline, with confident correct detection of at least the left lane

### Observations on HSV filtered Kathmandu
- The mask produced almost entirely black output with no yellow or white regions detected anywhere in the frame
- Grayscale conversion received a nearly empty image
- Canny edge detection fired on the few remaining bright pixels from street lights and sky
- The ROI mask eliminated most of that remaining noise
- Hough line detection returned None on most frames because there were no edges to find
- When lines did appear, they tracked dashboard edges or random noise fragments, not lane markings
- Critically, the output no longer showed the confident, confidently wrong lines of the baseline pipeline
- The pipeline now fails silently by returning no output, which is the correct behavior when markings are absent

### Key finding from HSV filtering
HSV color filtering is a meaningful pre-processing improvement for structured roads with colored lane markings. On highway footage, it reduces false positives from urban clutter and stabilizes the detection of the left lane. More importantly, on Kathmandu footage it changes the failure mode from confident wrong output to silent failure. Instead of drawing wrong lines based on building edges, the pipeline produces no output when it finds no matching colors. This is a behavioral improvement but it does not solve the fundamental problem. The pipeline still cannot detect lanes where no markings exist, because there is literally nothing to filter for. The signal absence problem remains unchanged; we have only improved the behavior when signal is absent, not created signal where none exists.

### Images saved
- hsv_filtered_highway_yellow_clean.png: yellow lane marking isolated perfectly
- hsv_filtered_highway_white_dashed.png: white right lane captured in dash regions
- hsv_filtered_kathmandu_empty.png: almost entirely black, no colors matched
- comparison_baseline_vs_hsv_kathmandu.png: baseline shows confident wrong lines, HSV shows silent failure


# RoadVision Nepal Research Log

## Session 3 June 10, Wednesday

### What I learned

**Gaussian blur mechanics**
- Gaussian blur replaces each pixel with a weighted average of its surrounding pixels
- Closer pixels receive higher weights, while further pixels get lower weights
- The kernel size controls the neighborhood size and must be odd to have a clear center pixel
- Standard deviation (sigma) controls how steep the weight drop-off is
- Setting sigma=0 lets OpenCV auto-calculate it from the kernel size
- If the kernel is too large, it over-blurs and destroys genuine edges along with the noise

**Canny edge detection process**
- Canny is a multi-step pipeline: gradient computation (using Sobel) followed by non-maximum suppression, then double thresholding, then hysteresis
- Non-maximum suppression thins edges down to single-pixel-wide lines
- Two thresholds are used: above the high threshold = definite edge, below the low = discarded, in between = weak edge
- Hysteresis keeps weak edges only if they connect to a strong edge, creating chains
- If the low threshold is too low, noise chains connect to strong edges and pull in false edges
- The key insight: Canny is not failing in Kathmandu. The environment simply has no signal to give it

### What I built
- Added Stage 3: Gaussian blur to main.py with a 5x5 kernel and sigma=0
- Added Stage 4: Canny edge detection to main.py with thresholds 50/150
- Ran both pipelines simultaneously on Kathmandu and Highway footage for direct comparison
- Used cv.CAP_PROP_POS_MSEC to jump to timestamp 2:35:43 in the highway video to find a clean open road section

### Observations on Gaussian Blur (Kathmandu)
- Streetlamps and headlights remain dominant after blurring because their intensity is too strong to suppress
- The road surface remained unchanged, which confirms there are no gradients to blur
- Power lines became noticeably thinner and fainter; high-frequency features are most affected by blur
- This shows the blur step is working correctly on what it receives, but the input has no useful road signal to preserve

### Observations on Canny (Kathmandu)
- Dense edges appeared on buildings, power lines, utility poles, and vehicle outlines
- The road surface stayed completely black with zero edges detected
- Power lines survived not because of their own strength but through hysteresis chaining to building edges
- This confirmed the Session 2 prediction: Canny fires on urban infrastructure before any road-relevant features

### Highway vs Kathmandu comparison
- Highway: two clean diagonal lines in the lower frame, the yellow left line and dashed white right line clearly detected
- Highway upper half was mostly black, with open sky and road producing almost nothing
- Kathmandu: dense edges everywhere except on the road surface itself
- Same pipeline, same thresholds, opposite results
- Highway gives the pipeline exactly what it needs; Kathmandu gives everything except what it needs

### Key finding from Stage 4
Canny is not failing. The classical pipeline is working as designed. The failure is environmental. No lane markings means no intensity gradients on the road surface, which means there is nothing for the algorithm to find. This is a fundamental mismatch between the pipeline's assumptions and the environment, not a parameter tuning problem.

### Images saved
- canny_kathmandu_urban_failure.png: dense building edges with the road surface black
- canny_comparison_kathmandu_vs_highway.png: side-by-side comparison showing the core finding


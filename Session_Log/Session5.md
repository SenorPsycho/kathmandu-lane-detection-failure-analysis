## Session 5 June 13, Friday

### What I learned

**How the Hough Line Transform works**
- After Canny, you have white pixels scattered on a black image with no context connecting them
- Hough's job is to figure out which pixels belong to the same line
- Every white pixel votes for all possible lines that could pass through it
- Lines that receive many votes from many pixels are real lines, and lines with few votes are noise
- This voting approach has been called "a democracy of pixels"

**HoughLines vs HoughLinesP**
- HoughLines returns infinite lines that stretch across the entire frame, which is not useful for lane detection
- HoughLinesP is probabilistic and returns actual line segments with start and end points (x1, y1, x2, y2)
- HoughLinesP is the standard choice for lane detection pipelines

**HoughLinesP parameters explained**
- rho=2: precision of the distance voting grid; 2 pixels is the standard value
- theta=np.pi/180: 1-degree angle precision; always use this
- threshold=100: minimum votes needed for a line to be returned; higher is stricter
- minLineLength=40: segments shorter than this get discarded to remove noise
- maxLineGap=5: gaps smaller than this between aligned segments get bridged, helping with dashed lines
- Dashed lines need lower threshold and minLineLength than solid lines because each dash is short and receives fewer votes

**Drawing lines with cv.line**
- Takes parameters: image, pt1 (x1,y1), pt2 (x2,y2), color (BGR tuple), thickness
- Always draw on a copy of the frame to preserve the original for comparison
- HoughLinesP output is wrapped in an extra array layer, so use line[0] to unwrap to x1,y1,x2,y2

**Handling missing results**
- HoughLinesP returns None if no lines are detected
- Always check if result is not None before looping, otherwise the code will crash
- On Kathmandu frames this None check fires frequently

### What I built
- Added Stage 6: HoughLinesP applied to both ROI outputs
- Added separate loops for Kathmandu and Highway with None checks
- Lines drawn in green on frame copies, preserving the original frames
- Both videos running simultaneously for direct comparison
- Output files: output_kathmandu.mp4 and output_highway.mp4

### Observations on Hough Lines (Highway)
- The yellow left lane line was detected cleanly as a long diagonal green segment following it precisely
- The white dashed right lane was partially detected as shorter segments; gaps between dashes were not fully bridged
- Some false detections appeared on vegetation and distant vehicles inside the ROI
- The pipeline worked correctly on this structured road environment

### Observations on Hough Lines (Kathmandu)
- A horizontal green line at the bottom detected the dashboard edge, not a lane
- Few random short segments appeared from building edges and vehicles inside the ROI triangle
- No consistent diagonal lane lines appeared anywhere
- The road surface produced no detections, confirming all previous stage findings

### Key finding from Stage 6
The Hough Line Transform completes the failure picture. On the highway, the pipeline returns clean lane line segments. On Kathmandu, it returns dashboard edges and random noise fragments. The absence of lane markings propagates through every stage: no gradients at Canny, no edges at ROI, no lines at Hough. The pipeline cannot invent signal that was never there.

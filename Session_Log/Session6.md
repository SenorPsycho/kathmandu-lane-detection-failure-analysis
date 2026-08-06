## Session 6 June 14, Saturday

### What I learned

**Line averaging core concept**
- Hough returns many short segments per frame for what should be two lane lines
- Averaging groups all segments into left lane and right lane based on slope direction
- Negative slope represents the left lane, positive slope represents the right lane (because y increases downward in OpenCV)
- Lines with slope between -0.3 and 0.3 are nearly horizontal and are treated as noise and discarded
- All slopes and intercepts per side get averaged into one representative slope and intercept
- np.average() with axis=0 averages columns separately: all slopes together, all intercepts together

**Slope and intercept**
- Slope = (y2 - y1) / (x2 - x1), which represents the steepness of the line
- Intercept = y1 - slope * x1, which tells where the line crosses the y-axis
- Together they describe any line using the equation y = mx + b

**Converting slope and intercept back to pixel coordinates**
- cv.line needs two points, not slope and intercept
- Fix y1 at the frame bottom (height) and y2 at 60% of height (near the horizon)
- Solve for x using x = (y - intercept) / slope
- int() wraps the result because pixel coordinates must be whole numbers
- The function returns a tuple (x1, y1, x2, y2), which is immutable

**Defensive programming and None handling**
- average_line returns None for a side if no lines of that slope direction were found
- make_line returns None early if passed None
- Every drawing block checks is not None before unpacking and drawing
- This defensive approach prevents the pipeline from crashing on empty frames

**Two distinct failure modes identified**
- Signal discontinuity: marking exists but isn't always visible (like the dashed white highway line flickering)
- Signal absence: nothing consistent to track at all (like the Kathmandu lines jumping every frame)
- These are different problems; one is fixable with temporal smoothing, one is not

### What I built
- Added Stage 7: average_line() function to group Hough segments by slope and average into one line per side
- Added Stage 7: make_line() function to convert averaged slope and intercept to drawable pixel coordinates
- Replaced raw Hough drawing loops with averaged single lines per side
- Both videos running simultaneously, each drawing up to two averaged green lines per frame

### Observations on Averaged Lines (Highway)
- Two clean lines converged toward a vanishing point on the horizon
- The left line tracked the yellow lane marking consistently
- The right line tracked the white dashed marking but flickered on frames between dashes
- Lines crossed near the horizon with geometrically correct perspective behavior
- The pipeline produced stable, meaningful output on structured roads

### Observations on Averaged Lines (Kathmandu)
- Two lines were drawn but they tracked building edges and vehicle outlines, not lane markings
- Lines jumped to different angles and positions every few frames with no consistent anchor
- Lines crossed in the middle of the frame, not at a road vanishing point
- The pipeline output looked confident and stable but was completely wrong
- Instability confirmed that no consistent signal existed for the averaging to converge on

### Key finding from Stage 7
The completed classical pipeline reveals its most important failure characteristic: it does not fail silently on Kathmandu footage. It draws lines every frame with apparent confidence. But those lines track building edges, vehicle outlines, and road boundaries, not lane markings, because none exist. A system relying on this output would not know it was wrong. This is more dangerous than returning no output at all. Signal absence produces confidently incorrect output, not null output.

### Images saved
- averaged_lines_comparison_1.png: both lanes detected on highway, Kathmandu lines tracking buildings
- averaged_lines_comparison_2.png: highway left lane clean, Kathmandu single line crossing frame diagonally

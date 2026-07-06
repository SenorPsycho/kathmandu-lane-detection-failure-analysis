# RoadVision Nepal Research Log

## Session 4 June 11, Thursday

### What I learned

**NumPy and image arrays**
- Images are stored as grids of numbers in NumPy arrays. Grayscale is 2D, color is 3D
- Every OpenCV frame is a NumPy array under the hood
- np.zeros_like(image) creates a black array with the exact same shape and data type as the input image
- Dimensions work as shape[0] = height, shape[1] = width (confirmed again in the context of masks)

**Masking fundamentals**
- A mask is a black image with a white shape drawn on it
- White regions keep pixels from the original image, black regions discard them
- cv.fillPoly() fills a polygon with a color on a given image
- Polygon points must be provided as a NumPy array

**Bitwise AND operation**
- Operates on a per-pixel basis, and both pixels must be white (255) for the result to be white
- 255 AND 255 = 255 (edge survives)
- 255 AND 0 = 0 (edge is removed)
- Used to combine Canny output with the mask so only edges inside the white polygon survive

**Why a triangular ROI**
- From a dashcam perspective, the road occupies a triangle shape: wide at the bottom, narrow at the horizon
- A rectangle would include buildings and parked vehicles on the sides, which is unnecessary
- A triangle cuts directly to the road region ahead, removing irrelevant edges from the frame edges

### What I built
- Added Stage 5: region_of_interest() function to main.py
- Defined the triangle with three points: bottom-left (0, 1080), bottom-right (1920, 1080), apex (960, 540)
- Applied it to the Canny output for both Kathmandu and Highway footage
- Ran both videos simultaneously for direct comparison
- Set the Highway timestamp to 2:35:43 to find an open road section with clear lane markings and minimal urban clutter

### Observations on ROI (Highway)
- Two clean diagonal lines were visible inside the triangle: the yellow left line and dashed white right line
- Lines converged toward the apex as expected from perspective
- Some vegetation edges appeared on the left side, but the lane lines were clearly dominant
- ROI masking successfully isolated the road region the pipeline was designed for

### Observations on ROI (Kathmandu)
- Buildings and vehicles survived inside the lower triangle because the urban scene extends into the road region
- The road surface at the bottom showed only a faint horizontal boundary line, not a lane marking
- No diagonal lane lines appeared anywhere inside the triangle
- The road surface area inside the triangle was empty, with no edges

### Key finding from Stage 5
ROI masking confirms that the failure is not about noise in the frame. Sky, power lines, and upper-frame clutter were all eliminated. Even with perfect isolation of the road region, there are no lane edges inside the triangle on Kathmandu footage. The absence of markings means no edges exist where the pipeline looks for them. This is not a fixable parameter; it is a structural mismatch between the pipeline's assumptions and the environment.


# RoadVision Nepal Research Log

## Session 2 June 09, Tuesday

### What I learned

**Color and grayscale basics**
- BGR stands for Blue Green Red, the color representation OpenCV uses internally
- Grayscale converts all three color channels into a single intensity channel
- The grayscale formula is: Gray = 0.114*Blue + 0.587*Green + 0.299*Red
- Green has the highest weight because human eyes are most sensitive to green wavelengths
- This means color differences in the original image can survive grayscale conversion, just at different intensities
- Image dimensions work as shape[0] = height, shape[1] = width, shape[2] = channels (for color)

**Working with different color spaces**
- HSV cannot convert directly to grayscale; it has to go through BGR first (HSV > BGR > Gray)
- Matplotlib expects RGB input, but OpenCV uses BGR internally, so conversion is needed before plotting
- This matters for debugging because the colors will be off otherwise

### What I built
- Added Stage 2: Grayscale conversion to main.py
- Created a rescale_frame function to display footage at 0.5 scale for faster processing
- Wrote practice/color_spaces.py to explore BGR, HSV, LAB, and RGB conversions side by side

### Observations on Kathmandu grayscale
- The road surface maps to a uniform dark gray with no visible intensity gradients
- No lane markings means there is nothing to create those gradients
- The dominant bright regions in the image are streetlamps, headlights, and the sky
- This early finding suggests Canny edge detection will fire on lighting and building edges long before it finds anything road-relevant
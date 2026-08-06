## Session 7 June 16, Monday

### What I learned

**cv.VideoWriter basics**
- Takes four arguments: output file path, codec, fps, and frame size as a tuple (width, height)
- Must be initialized before the while loop; creating it inside the loop resets the file every frame
- Frame size must match the actual frame dimensions exactly; mismatches corrupt the output file
- Release the writer after the loop, just like VideoCapture, following the same pattern

**FourCC codes**
- Four character code that specifies the video codec, which handles compression and encoding
- cv.VideoWriter_fourcc(*'mp4v') is used for .mp4 output
- The * unpacks the string into four separate characters as required by the function

**FPS matching**
- Output FPS must match input FPS; mismatches cause slow motion, fast forward, or choppy playback
- Retrieve FPS from VideoCapture using cv.CAP_PROP_FPS before the loop
- Each video gets its own FPS variable in case they differ

**Frame dimensions from VideoCapture**
- Retrieved using cv.CAP_PROP_FRAME_WIDTH and cv.CAP_PROP_FRAME_HEIGHT
- Must wrap in int() because the property returns a float, but VideoWriter requires integers
- Retrieve these from the VideoCapture object before the loop, not from frames inside the loop

### What I built
- Added Stage 8: VideoWriter initialized for both Kathmandu and Highway outputs
- Processed frame copies written to Output/ folder each loop iteration
- Both writers released properly after the loop alongside VideoCapture objects
- Output files: Output/output_kathmandu.mp4 and Output/output_highway.mp4
- The classical pipeline is now complete with all 8 stages built and running

### Observations from output videos
- Kathmandu output: lines flicker to different angles every frame, tracking building edges and noise with no consistent lane detection throughout the entire video
- Highway output: left lane line stable and consistently tracking the yellow marking; right dashed line flickers between frames, sometimes replaced by the outer shoulder line when dashes disappear
- Highway occasionally catches the shoulder line instead of the dashed center line because the ROI triangle is wide enough to include the road shoulder

### Key finding from Stage 8 and baseline complete
The completed classical pipeline produces two qualitatively different outputs. Highway shows stable left lane detection with partially stable right lane detection and occasional false positives from the road shoulder. Kathmandu shows no lane detection at any point in the video; lines are present every frame but tracking noise sources only. The pipeline cannot be tuned to work on Kathmandu footage because there is no parameter adjustment that creates signal where none exists in the environment. This completes the classical baseline. All subsequent work builds on this documented failure.
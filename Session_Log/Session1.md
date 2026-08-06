# RoadVision Nepal Research Log

## Session 1 June 08, Monday

### What I set up
- Created the project folder structure
- Downloaded two video samples for contrast:
  - highway.mp4: US highway with clear lane markings and good lighting
  - kathmandu.mp4: Kathmandu urban road with no lane markings and dusk lighting
- Wrote main.py to load and display the Kathmandu video using OpenCV
- Initialized a new repo and committed the initial setup

### First observations on the footage
The Kathmandu footage shows multiple failure conditions right from frame 1: no lane markings, power lines crossing the frame, mixed traffic, and low light. The highway footage, by contrast, has clear yellow left line and dashed white right line with strong contrast between the markings and the dark asphalt. This difference will be the baseline for the entire analysis.

### Research direction
The goal is to understand exactly how and why the classical lane detection pipeline fails on unstructured roads like those in Kathmandu, not just to document that it fails. By running the same pipeline on both videos in parallel, we can isolate environmental factors from algorithm factors.

## Session 8 June 17, Wednesday

### What I did
- Started FAILURE_ANALYSIS.md and wrote the Overview section
- Created the Pipeline Assumptions vs Environment Reality table to compare highway conditions with Kathmandu conditions
- Identified four core assumption categories: lane marking contrast, lighting conditions, urban edge clutter, and road boundary visibility
- Sharpened the table content to reference specific mechanisms from earlier sessions (like hysteresis chaining onto building edges and headlight blowout creating false gradients, rather than generic "noise" language)
- Ran a full codebase review using Copilot on main.py, the folder structure, and all session logs
- Identified and fixed two robustness issues: missing isOpened() checks on both VideoCapture objects, and a missing slope guard in make_line() to prevent divide-by-zero errors on near-zero slopes

### Findings from the code review
- Core pipeline logic and research framing are solid; the failure is environmental, not a misuse of OpenCV
- Missing elements: README.md, requirements.txt, consistent file naming conventions, and the completed FAILURE_ANALYSIS.md
- Several review suggestions (quantitative metrics, related work citations) are valid in general but were intentionally deferred because qualitative analysis was the deliberate choice given no ground truth labels exist
- Confirmed roadmap: finish FAILURE_ANALYSIS.md next, then move to the adaptations phase, then polish phase (README, cleanup)

### Robustness fixes applied
- Added isOpened() checks before accessing video properties to prevent crashes on corrupted or missing files
- Added a slope guard in make_line() to handle cases where slope is very close to zero, which would cause division errors

### What this means
The classical baseline is now fully documented with analysis. The failures are understood at a mechanistic level, not just observed. The pipeline is now robust enough to handle edge cases without crashing. We are ready to move into the adaptation phase, which will explore whether alternative approaches (like HSV color filtering or boundary detection) can recover any usable signal on Kathmandu footage.


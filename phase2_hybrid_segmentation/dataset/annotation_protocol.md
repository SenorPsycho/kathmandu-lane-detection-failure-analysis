# Annotation Protocol — RoadVision Nepal Phase 2

## Task
Binary semantic segmentation: label each frame into two classes.

- **Drivable** — any surface a vehicle could currently physically traverse in this exact frame, regardless of paint, formal lane markings, or surface type.
- **Non-drivable** — everything else.

This is a binary task by design. Earlier multi-class hierarchies (e.g. IDD's 7-class scheme) were considered and rejected for this dataset's scale — see `dataset_README.md` for reasoning.

## Tool
**CVAT** (Computer Vision Annotation Tool), polygon-based annotation.
- Draw a closed polygon around the boundary of the drivable region(s) in each frame.
- Export format: COCO segmentation / mask PNGs (finalize based on what the training pipeline consumes — confirm before bulk export).

## Core Definition
Drivable = the surface a vehicle could physically and immediately drive on, as observed in this specific frame — not what is designated a "road" in general, and not what could become drivable if an obstacle moved.

Label based on the frame as it is, not what it usually looks like or what it will look like a moment later.

## Edge Case Rules

| Situation | Label | Reasoning |
|---|---|---|
| Main paved road surface | Drivable | Core case |
| Unpaved shoulder/dirt extension, actively being used by visible vehicles in frame | Drivable | Usage evidence overrides lack of paving |
| Unpaved shoulder/dirt extension, no visible use in frame | Non-drivable | Err toward only labeling evidently usable surface |
| Parked vehicle sitting on the road | Non-drivable (at that location) | Space is currently occupied; label the scene as-is |
| Moving vehicle in the frame | Non-drivable at its exact footprint; road behind/around it (if visible) remains drivable | Distinguish the obstacle from the surface it sits on |
| Pedestrian, animal, or any object on the road surface | Non-drivable at its footprint | Same logic as parked vehicles |
| Sidewalk, even if unbarricaded and walkable-width for a bike | Non-drivable | Not intended for vehicle traffic |
| Heavily shadowed or low-contrast road areas | Drivable, if boundary is inferable from context (continuation of a road you can see clearly elsewhere in frame) | Use surrounding context; don't guess wildly if genuinely ambiguous — see "Skip" rule below |
| Standing water / flooded sections of road | Drivable, unless clearly impassable (deep flooding, visible submersion) | Use judgment; note ambiguous cases in the frame log |
| Road exiting frame into blur/distance | Drivable up to the point it's visually indiscernible | Don't extrapolate beyond what's visible |
| Construction/rubble blocking part of the road | Non-drivable for the blocked section only | Partial occlusion, not full-frame exclusion |

## Skip Rule
If a frame is too ambiguous, too blurry, or the drivable boundary genuinely cannot be determined with reasonable confidence — **skip it and log it** (see below) rather than forcing a guess. A smaller set of confident labels is better than a larger set of noisy ones.

## Frame Logging
Maintain a simple log (CSV or spreadsheet) per frame with:
- Source video ID
- Timestamp in source video
- Condition tags (lighting, traffic level, stability/quality)
- Status: labeled / skipped (with 1-line reason if skipped)

This log becomes the basis for the condition-distribution stats in `dataset_README.md` and lets you reconstruct train/val/test splits by source video and time chunk later.

## Consistency Check
Before annotating in bulk, label ~10 frames, set them aside, and re-label them again a few days later without looking at the originals. Compare. This catches drift in your own labeling standards early, before it's baked into hundreds of frames. Document any definition changes that come out of this in this file (version the changes, don't silently redefine).

## Versioning
This protocol may evolve as edge cases are discovered during annotation. Log changes at the bottom of this file with a date, rather than editing rules silently once frames have already been labeled under the old rule.

---
### Change Log
- v1.0 — initial protocol drafted.

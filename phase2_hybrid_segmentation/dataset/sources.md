# Sources — RoadVision Nepal Phase 2 Dataset

Provenance record for all raw footage used in dataset construction. Fill in blanks as each video is confirmed. This file supports the licensing/attribution check before any derived frames are published, and lets the dataset README cite sources accurately.

| # | Local filename | YouTube Title | Channel | URL | Length (usable, Kathmandu-relevant) | Condition tags | License / reuse terms noted | Attribution required? |
|---|---|---|---|---|---|---|---|---|
| 1 | | Kathmandu to Dharke Drive in Nepal via Sitapaila-Dharke road. POV Drive. ASMR | | https://www.youtube.com/watch?v=FWbcMCDHzYI | ~20 min (trimmed to Kathmandu portion; confirmed cutoff 33:15; 200 frames extracted) | Dusk, low traffic, stable | | |
| 2 | Driving in Nepal - Kathmandu.mp4 | | | https://www.youtube.com/watch?v=dCPV-5JeJC0 | | Sunny, crowded urban traffic | | 35 frames extracted. 6-second intro skipped during extraction. Frames outside city/valley limits and frames with near-total road occlusion (e.g. large vehicle filling frame) were manually reviewed and excluded. |
| 3 | | | | https://www.youtube.com/watch?v=3QXDap1_Rmk | Sunrise/early morning continuous drive (full valley coverage) | Sunrise, light traffic, full coverage | | Attribution: "eye.&.i" watermark; 778 frames extracted (2s sampling interval) from `v03_final/` |
| 4 | DRIVING TOUR: Beautiful KATHMANDU Road.mp4 | DRIVING TOUR: Beautiful KATHMANDU Road | | https://www.youtube.com/watch?v=mxgsjzBNw_s | ~32:48; CapCut watermark | Sunny→mixed conditions, light→heavy traffic, narrow streets + highway sections | | Finalized review set: 493 frames retained in `extracted_frames/v04_final/` after blur screening and manual boundary-traceability review. The clean/stress split was dropped; only the single final set remains, and mildly blurry frames were kept only where the drivable/non-drivable boundary was clearly traceable. |
| 5 | | | | https://www.youtube.com/watch?v=9_6NVmgiKhI | | Daytime, sunny, standard non-fisheye camera, mixed light-to-heavy traffic | | Finalized with no caveats; all 3 review samples matched the stated conditions with no issues found. |
| 6 | | | | https://www.youtube.com/watch?v=Kb1kE5uNbww | | Excluded from final dataset (dashcam footage with burned-in telemetry overlay and fisheye/barrel distortion) | | Excluded entirely from the final dataset because the footage is dashcam-based with burned-in telemetry overlay and fisheye/barrel distortion, which is inconsistent with the standard non-fisheye geometry used elsewhere. |
| 7 | | Driving Kathmandu City 4K \| Morning Drive \| Nepal | | https://www.youtube.com/watch?v=yIcOxLrFVGg | | Hazy/smog conditions (warm orange-brown haze reducing contrast and visibility at distance; confirmed via 3 review samples) | | Finalized; condition label corrected from “Overcast” to “Hazy/smog conditions,” with 218 frames retained in `extracted_frames/v07_final/`. |

## Fields to confirm per video
- **Local filename** — exact name yt-dlp saved it as in `raw_footage/`
- **Channel** — creator name shown on the video page
- **License / reuse terms noted** — check the video description and the channel's about page; note "Standard YouTube License" if nothing else is stated, or the specific terms (e.g. Creative Commons) if the creator specifies one
- **Attribution required?** — yes/no, and what form (e.g. "credit channel name + link in dataset README")

## Notes
- Videos originally referenced as "New #1" through "New #4," "Evening ride," "Overcast," and "Kathmandu–Hetauda" in project planning correspond to entries 2–6 above — match by condition description once each URL is opened and confirmed.
- Any video without a clearly stated reuse license should be treated conservatively: attribute the source clearly in the dataset README regardless, and consider reaching out to the creator for explicit permission before public release if terms are ambiguous.
- Update this table before frame extraction begins for each video, not after — this is the checkpoint for the licensing review, not a retroactive formality.

Grand total for the finalized dataset (Videos 1–5 and 7; Video 6 excluded): 2,304 frames, based on the verified counts in the final extracted frame folders.

---
*Last updated: finalized for Videos 1–7; Video 6 excluded from the dataset total.*

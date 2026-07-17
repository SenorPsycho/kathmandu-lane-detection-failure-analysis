# Sources — RoadVision Nepal Phase 2 Dataset

Provenance record for all raw footage used in dataset construction. Fill in blanks as each video is confirmed. This file supports the licensing/attribution check before any derived frames are published, and lets the dataset README cite sources accurately.

| # | Local filename | YouTube Title | Channel | URL | Length (usable, Kathmandu-relevant) | Condition tags | License / reuse terms noted | Attribution required? |
|---|---|---|---|---|---|---|---|---|
| 1 | | Kathmandu to Dharke Drive in Nepal via Sitapaila-Dharke road. POV Drive. ASMR | | https://www.youtube.com/watch?v=FWbcMCDHzYI | ~20 min (trimmed to Kathmandu portion; confirmed cutoff 33:15; 200 frames extracted) | Dusk, low traffic, stable | | |
| 2 | Driving in Nepal - Kathmandu.mp4 | | | https://www.youtube.com/watch?v=dCPV-5JeJC0 | | Sunny, crowded urban traffic | | 35 frames extracted. 6-second intro skipped during extraction. Frames outside city/valley limits and frames with near-total road occlusion (e.g. large vehicle filling frame) were manually reviewed and excluded. |
| 3 | | | | https://www.youtube.com/watch?v=3QXDap1_Rmk | Sunrise/early morning continuous drive (full valley coverage) | Sunrise, light traffic, full coverage | | Attribution: "eye.&.i" watermark; 778 frames extracted (2s sampling interval) from `v03_final/` |
| 4 | | DRIVING TOUR: Beautiful KATHMANDU Road | | https://www.youtube.com/watch?v=mxgsjzBNw_s | ~32:48; CapCut watermark | Sunny→overcast (mixed), light→heavy traffic, narrow streets + highway sections | | 2s sampling interval. Final frame count: 870 retained in extracted_frames/v04_review/; clean/degraded split not yet finalized. Planned final folders: v04_final/clean/ and v04_final/degraded/. |
| 5 | | | | https://www.youtube.com/watch?v=9_6NVmgiKhI | | | | |
| 6 | | | | https://www.youtube.com/watch?v=Kb1kE5uNbww | | | | |
| 7 | | Driving Kathmandu City 4K \| Morning Drive \| Nepal | | https://www.youtube.com/watch?v=yIcOxLrFVGg | | | | |

## Fields to confirm per video
- **Local filename** — exact name yt-dlp saved it as in `raw_footage/`
- **Channel** — creator name shown on the video page
- **License / reuse terms noted** — check the video description and the channel's about page; note "Standard YouTube License" if nothing else is stated, or the specific terms (e.g. Creative Commons) if the creator specifies one
- **Attribution required?** — yes/no, and what form (e.g. "credit channel name + link in dataset README")

## Notes
- Videos originally referenced as "New #1" through "New #4," "Evening ride," "Overcast," and "Kathmandu–Hetauda" in project planning correspond to entries 2–6 above — match by condition description once each URL is opened and confirmed.
- Any video without a clearly stated reuse license should be treated conservatively: attribute the source clearly in the dataset README regardless, and consider reaching out to the creator for explicit permission before public release if terms are ambiguous.
- Update this table before frame extraction begins for each video, not after — this is the checkpoint for the licensing review, not a retroactive formality.

---
*Last updated: pending full confirmation of all 7 entries.*

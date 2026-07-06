# Road Vision Nepal

This repository is being used for a dataset and ablation study on drivable-area segmentation for unmarked Kathmandu roads.

## Current focus

We are investigating whether classical computer-vision priors can improve deep learning segmentation on roads where lane markings are absent or weak. In particular, we are testing whether priors such as edge maps and HSV-based filtering provide useful signal for identifying drivable regions in Kathmandu scenes.

## Research question

Do classical vision cues, informed by a documented failure analysis of conventional lane-detection pipelines, improve deep-learning drivable-area segmentation on unmarked or weakly marked roads?

## Motivation

Classical lane-detection systems often assume the presence of painted lane markings, strong contrast, and structured road geometry. Those assumptions break down on many Kathmandu roads. This study examines whether simple priors can still help a modern segmentation model under those conditions.

## Study design

The work is organized as an ablation study comparing segmentation performance under different input conditions:

- Baseline segmentation model
- Edge-map prior augmentation
- HSV filtering prior augmentation
- Combined edge + HSV priors

The design is informed by the failure analysis documented in [FAILURE_ANALYSIS.md](FAILURE_ANALYSIS.md), which outlines how classical pipelines fail when lane markings are absent and irrelevant edges dominate the scene.

## Dataset

The project uses road imagery from Kathmandu and related unstructured urban scenes, with an emphasis on:

- Unmarked or weakly marked roads
- Complex roadside structure
- Mixed lighting and clutter
- Drivable-area labels for segmentation evaluation

## Expected outcome

The goal is not to claim that classical priors are universally sufficient, but to test whether they provide measurable value in a difficult setting where standard lane-detection assumptions do not hold.

## Repository purpose

This repository currently contains the experiment code, analysis notes, and supporting material for the segmentation ablation study. The README will be refined later as the work matures.

## Stack

Python, OpenCV, NumPy, PyTorch-style segmentation workflows (subject to the current implementation)


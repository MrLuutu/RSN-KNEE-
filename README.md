# RSNA Knee Abnormality Detection

Machine learning project for the **RSNA Knee Abnormality Detection** Kaggle challenge.

## Challenge

The objective is to detect abnormalities in knee MRI studies using multimodal DICOM imaging data.

**Kaggle:** https://www.kaggle.com/competitions/rsna-knee-abnormality-detection/overview

## Repository Structure

```text
RSN-KNEE-
├── configs/
├── notebooks/
├── outputs/
├── rsna-knee-abnormality-detection/
├── src/
│   ├── data/
│   ├── preprocessing/
│   ├── models/
│   └── evaluation/
├── tests/
├── .gitignore
├── LICENSE
├── Project-Status.md
└── README.md
```

## Pipeline

```text
DICOM
  ↓
Study
  ↓
Series
  ↓
Slice Ordering
  ↓
Preprocessing
  ↓
Model
  ↓
Study-Level Prediction
  ↓
Evaluation
```

## Current Stage

Repository setup and DICOM data exploration are complete.

The next technical stage is to establish a reproducible MRI preprocessing pipeline before model training.

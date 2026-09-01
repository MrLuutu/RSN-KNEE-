# RSNA Knee Abnormality Detection

**Kaggle:** https://www.kaggle.com/competitions/rsna-knee-abnormality-detection/overview
**GitHub:** https://github.com/MrLuutu/RSN-KNEE-

## Status

* Dataset downloaded and explored
* DICOM files successfully loaded
* MRI studies, series, dimensions, and labels examined
* DICOM loader added to the repository
* `._` macOS files excluded

## Current Problem

Define a reliable pipeline for converting each knee MRI study into model input:

`DICOM → Series → Slice Ordering → Preprocessing → Model`

## Next Step

Build a baseline model after deciding:

* Slice ordering
* Image preprocessing
* Sequence handling
* Study-level train/validation splits

**Seeking advice on the MRI preprocessing and model architecture before training begins.**


NEXT STEP
Investigate the existing MRI series and determine the first
preprocessing approach.


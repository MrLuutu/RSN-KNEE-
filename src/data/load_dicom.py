from pathlib import Path
import pydicom


def load_series(series_path):
    files = sorted(
        file
        for file in Path(series_path).glob("*.dcm")
        if not file.name.startswith("._")
    )

    if not files:
        raise FileNotFoundError(f"No DICOM files found: {series_path}")

    return [
        pydicom.dcmread(file, stop_before_pixels=True, force=True)
        for file in files
    ]


if __name__ == "__main__":
    train_path = Path("rsna-knee-abnormality-detection/train_series")
    first_dicom = next(
        file
        for file in train_path.rglob("*.dcm")
        if not file.name.startswith("._")
    )

    series_path = first_dicom.parent
    slices = load_series(series_path)

    print(f"Series: {series_path}")
    print(f"Actual DICOM files: {len(slices)}")

    for tag in [
        "SeriesInstanceUID",
        "SeriesDescription",
        "Modality",
        "InstanceNumber",
        "ImagePositionPatient",
        "ImageOrientationPatient",
        "SliceLocation",
        "Rows",
        "Columns",
    ]:
        present = sum(hasattr(ds, tag) for ds in slices)
        print(f"{tag}: {present}/{len(slices)} present")
# Coding challenge

Part1: Code to read and parse DICOM files and contours, and batch the resulting data for feeding into a machine learning pipeline.

Part2: Parsing of outer countours. Thresholding methods for segmentation.

- `integration_test.py` shows an example usage and also serves as an integration test.
- `parsing_test.py`, `reading_test.py` and `feeding_test.py`, `thresholding_test.py` contain unit tests for various functions.
- `analysis.ipynb` explores thresholding approaches.

## Prerequisites:

Make sure that the `final_data/` folder exists in the parent directory.

## Requirements:

You will need the following python packages:
        Numpy, Pillow, pydicom, matplotlib

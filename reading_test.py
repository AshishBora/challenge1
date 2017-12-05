"""Tests for functions in reading.py"""

import reading


def test_get_patients():
    """Check if all patients are obtained from linking file."""
    link_filepath = './final_data/link.csv'
    patients = reading.get_patients(link_filepath)
    assert len(patients) == 5


def test_get_dicom_paths(patient):
    """Check if all dicom files are read"""
    dicom_paths_dict = reading.get_dicom_paths(patient)
    assert len(dicom_paths_dict.keys()) == 240


def test_get_icontour_paths(patient):
    """Check if all icountour files are read"""
    icontour_paths_dict = reading.get_icontour_paths(patient)
    assert len(icontour_paths_dict.keys()) == 18


def test_intersect():
    """Check if intersection works as intended"""
    dict1 = {1: 'a', 2: 'b'}
    dict2 = {2: 'c', 3: 'd'}
    common_keys = reading.intersect(dict1, dict2)
    assert len(common_keys) == 1
    assert list(common_keys)[0] == 2


def test_read_data():
    """Check if images and targets have the correct size and values"""
    dicom_path = './final_data/dicoms/SCD0000101/128.dcm'
    icontour_path = './final_data/contourfiles/SC-HF-I-1/i-contours/IM-0001-0128-icontour-manual.txt'
    image, target = reading.read_data(dicom_path, icontour_path)
    assert image.shape == (256, 256)
    assert target.shape == (256, 256)
    assert set(target.flatten()) == {True, False}


def main():
    """Run all tests."""

    patient_id = 'SCD0000101'
    original_id = 'SC-HF-I-1'
    patient = reading.Patient(patient_id, original_id)

    test_get_patients()
    test_get_dicom_paths(patient)
    test_get_icontour_paths(patient)
    test_intersect()
    test_read_data()


if __name__ == '__main__':
    main()
    print 'Passed all asserts'

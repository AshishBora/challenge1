"""Read and link data from appropriate files"""

import glob
import parsing


class Patient(object):
    """Class to represent a patient"""
    def __init__(self, patient_id, original_id):
        self.patient_id = patient_id
        self.original_id = original_id

    def pprint(self):
        """Pretty printing. Useful for debugging."""
        print 'patient_id = {}, original_id = {}'.format(self.patient_id, self.original_id)


class Datapoint(object):
    """Class to represent a patient, a dicom image, and the associated icontour"""
    def __init__(self, patient, dicom, icontour):
        self.patient = patient
        self.dicom = dicom
        self.icontour = icontour


def get_patients(link_filepath):
    """Read the link file and create patients

    :param link_filepath: filepath to the link file
    :return: list of Patient objects
    """
    with open(link_filepath, 'rb') as infile:
        lines = infile.readlines()
    lines = [line.strip().split(',') for line in lines[1:]]
    patients = [Patient(pid, oid) for pid, oid in lines]
    return patients


def parse_dir(prefix, suffix):
    """Glob with a given prefix and suffix and create dict middle part as the key

    :param prefix: prefix string
    :param suffix: suffix string
    :return: dict of matching paths with middle part as key
    """
    pattern = prefix + '*' + suffix
    paths = glob.glob(pattern)
    paths_dict = {}
    for path in paths:
        file_id = int(path[len(prefix):-len(suffix)])
        paths_dict[file_id] = path
    return paths_dict


def get_dicom_paths(patient):
    """Run parse_dir for dicoms

    :param patient: Patient object
    :return: paths to dicom files for that patient
    """
    prefix = './final_data/dicoms/{}/'.format(patient.patient_id)
    suffix = '.dcm'
    dicom_paths_dict = parse_dir(prefix, suffix)
    return dicom_paths_dict


def get_icontour_paths(patient):
    """Run parse_dir for icontours
    :param patient: Patient object
    :return: paths to icountour files for that patient
    """

    # Not sure what IM-0001 stands for. Can this change in the future?
    prefix = './final_data/contourfiles/{}/i-contours/IM-0001-'.format(patient.original_id)
    suffix = '-icontour-manual.txt'
    icontour_paths_dict = parse_dir(prefix, suffix)
    return icontour_paths_dict


def intersect(dict1, dict2):
    """Get common keys from two dictionaries

    :param dict1: python dict
    :param dict2: python dict
    :return: set of keys common to both dicts
    """
    keys1 = dict1.keys()
    keys2 = dict2.keys()
    common_keys = set(keys1) & set(keys2)
    return common_keys


def read_data(dicom_path, icontour_path):
    """Read the dicom images and icountours from disk

    :param dicom_path: filepath to dicom file
    :param icontour_path: filepath to icountour file
    :return: dicom image, mask created using icountour file
    """
    dcm_dict = parsing.parse_dicom_file(dicom_path)
    width, height = dcm_dict['pixel_data'].shape
    polygon = parsing.parse_contour_file(icontour_path)
    mask = parsing.poly_to_mask(polygon, width, height)
    return (dcm_dict['pixel_data'], mask)


def get_common_data(common_keys, dicom_paths_dict, icontour_paths_dict):
    """Read all data corresponding to one patient

    :param common_keys: set of keys
    :param dicom_paths_dict: dictionary mapping from keys to dicom image filepaths
    :param icontour_paths_dict: dictionary mapping from keys to icontour filepaths
    :return: a list of tuples of (image, target)
    """

    all_data = []
    for key in common_keys:
        dicom_path = dicom_paths_dict[key]
        icontour_path = icontour_paths_dict[key]
        data = read_data(dicom_path, icontour_path)
        all_data.append(data)
    return all_data


def get_datapoints(patient):
    """Create all datapoints for a patient

    :param patient: Patient object
    :return: a list of Datapoint objects
    """
    dicom_paths_dict = get_dicom_paths(patient)
    icontour_paths_dict = get_icontour_paths(patient)
    common_keys = intersect(dicom_paths_dict, icontour_paths_dict)
    common_data = get_common_data(common_keys, dicom_paths_dict, icontour_paths_dict)
    datapoints = [Datapoint(patient, dicom, icontour) for dicom, icontour in common_data]
    return datapoints

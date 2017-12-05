"""
1. DataFeeder to create batches of data
2. packaging function specific to images and contours
"""

import random
import numpy as np


class DataFeeder(object):
    """Generic class for batching data"""

    def __init__(self, data):
        self.data = data
        self.pos = 0
        self.total = len(data)
        self.shuffle() # initial shuffle

    def next_batch(self, batch_size):
        """Return the next data batch

        :param batch_size: size of the batch
        :return: list of data elements
        """
        if self.pos + batch_size > self.total:
            # if too few elements left, then shuffle
            self.shuffle()

        batch = self.data[self.pos: self.pos + batch_size]
        self.pos += batch_size
        return batch


    def shuffle(self):
        """Shuffle the data in-place"""
        random.shuffle(self.data)
        self.pos = 0  # reset position after shuffle


def package(datapoints):
    """Create numpy arrays of images and targets

    :param datapoints: list of Datapoint objects of length batch_size
    :return images: numpy array of size (batch_size, width, height)
    :return targets: numpy array of size (batch_size, width, height)
    """
    dicoms = [datapoint.dicom for datapoint in datapoints]
    icontours = [datapoint.icontour for datapoint in datapoints]
    images = np.stack(dicoms)
    targets = np.stack(icontours)
    return images, targets

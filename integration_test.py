"""A simple integration test"""

import reading
import feeding


def integration_test():
    """Read data for all patients and batch them."""

    link_filepath = './final_data/link.csv'
    patients = reading.get_patients(link_filepath)
    all_datapoints = []
    for patient in patients:
        datapoints = reading.get_datapoints(patient)
        all_datapoints.extend(datapoints)

    feeder = feeding.DataFeeder(all_datapoints)
    batch_size = 8
    for _ in range(100):
        datapoints = feeder.next_batch(batch_size)
        images, targets = feeding.package(datapoints)
        assert images.shape == (batch_size, 256, 256)
        assert targets.shape == (batch_size, 256, 256)


if __name__ == '__main__':
    integration_test()
    print 'Passed all asserts'


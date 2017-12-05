"""Test for code in feeding.py"""

import random
import feeding


def test_data_feeder():
    """Test if all data is being read and shuffled"""

    random.seed(0) # make the test deterministic

    data = list(range(64))
    data_feeder = feeding.DataFeeder(data)
    batch_size = 8

    # go over the dataset once
    data_so_far1 = []
    for _ in range(8):
        batch = data_feeder.next_batch(batch_size)
        data_so_far1.extend(batch)

    # Go over the dataset second time.
    # This should force shuffle
    data_so_far2 = []
    for _ in range(8):
        batch = data_feeder.next_batch(batch_size)
        data_so_far2.extend(batch)

    # all data was seen first time
    assert set(data_so_far1) == set(data)

    # all data was seen second time
    assert set(data_so_far2) == set(data)

    # data was shuffled in between
    assert data_so_far1 != data_so_far2


if __name__ == '__main__':
    test_data_feeder()
    print 'Passed all asserts'

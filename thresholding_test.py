"""Test for the function to find the best threshold"""

import thresholding


def test_find_best_thresh():
    """Mock test to get best threshold"""
    arr0 = [0, 1, 1, 2, 2, 3]
    arr1 = [2, 3, 3, 4, 4, 5]
    thresh, acc = thresholding.find_best_threshold(arr0, arr1)
    assert thresh == 2.5
    assert (acc - 0.83) < 0.01


if __name__ == '__main__':
    test_find_best_thresh()
    print 'Passed all asserts'

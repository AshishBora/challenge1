"""Find optimal threshold"""

import numpy as np


def find_best_threshold(arr0, arr1):
    """Find the best threshold seprating arr0 from arr1.

    We maximize the number of elements from arr0 that are less than or equal to
    the threshold plus the number of elements from arr1 that are greater than
    the threshold.

    :param arr0: list of numbers
    :param arr1: list of numbers
    :return thresh: Best separating threshold
    :return acc: Accuracy at the best threshold
    """

    # Use -1 for arr0 and 1 for arr1
    elems = [(num, -1) for num in arr0] + [(num, 1) for num in arr1]

    # Sort by original value
    elems.sort(key=lambda elem: elem[0])

    # Cumulative sum of +1 and -1s
    cumsum = np.cumsum([elem[1] for elem in elems])

    # best threshold = minimum cumulative sum
    # Averaging for finer estimation
    min_val = np.min(cumsum)
    min_pos = np.where(cumsum == min_val)[0]
    min_elems = [elems[pos][0] for pos in min_pos]
    thresh = np.mean(min_elems)

    # Compute accuracy
    acc = np.mean(list(arr0 <= thresh) + list(arr1 > thresh))

    return thresh, acc

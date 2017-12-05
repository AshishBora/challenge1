"""Tests for functions in parsing.py"""

import parsing


def test_parse_contour_file():
    """Test parsing of a contour file """
    filename = './test_countour.txt'
    coords_lst = parsing.parse_contour_file(filename)
    assert len(coords_lst) == 4


def test_poly_to_mask():
    polygon = [
        (64.0, 64.0),
        (64.0, 192.0),
        (192.0, 192.0),
        (192.0, 64.0)
    ]
    width, height = 256, 256
    mask = parsing.poly_to_mask(polygon, width, height)
    square = mask[65:192, 65:192]
    assert all(list(square.flatten()))


if __name__ == '__main__':
    test_parse_contour_file()
    test_poly_to_mask()
    print 'Passed all asserts'

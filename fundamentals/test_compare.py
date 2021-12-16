import pytest

from compare_lists import compare_lists

def test_compare():
    assert compare_lists([1, 2, 3], [1, 1, 1]) == 1
    assert compare_lists([1, 1, 1]) == 0
    assert compare_lists([1, 2, 3], [1, 3, 1]) == 2

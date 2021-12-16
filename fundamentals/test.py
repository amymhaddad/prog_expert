import pytest

from compare_lists import compare_lists
from trim_list import trim_list

def test_compare():
    assert compare_lists([1, 2, 3], [1, 1, 1]) == 1
    assert compare_lists([1, 1, 1]) == 0
    assert compare_lists([1, 2, 3], [1, 3, 1]) == 2

def test_trim():
    assert trim_list([1, 3, 34, "hi", "yes", True, 2.3], 3) == [1, 3, 34, "hi"]
    assert trim_list([True, False, 2.5, 6.2, 9.6, 2, 4], 2) == [True, False, 2.5, 6.2, 9.6]

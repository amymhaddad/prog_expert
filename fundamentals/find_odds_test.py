import pytest

from find_odds import odds

def test_odds():
    assert odds([1, 2, 3, 4, 5, 6, 5, 5, 3, 2]) == [1, 3, 5, 5, 5 , 3]


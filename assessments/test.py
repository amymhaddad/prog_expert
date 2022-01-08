import pytest

from cipher import caesar_cipher


def test_cipher():
    assert caesar_cipher("hello", 3) == "ebiil"
    assert caesar_cipher("apple", 5) == "vkkgz"
    assert caesar_cipher("tim", 2) == "rgk"

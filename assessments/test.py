import pytest

from cipher import caesar_cipher
from create_strings import create_strings_from_characters


def test_cipher():
    assert caesar_cipher("hello", 3) == "ebiil"
    assert caesar_cipher("apple", 5) == "vkkgz"
    assert caesar_cipher("tim", 2) == "rgk"


def test_create_strings():
    frequencies = {"a": 3, "b": 5, "c": 3, "d": 2, "e": 1}
    string1 = "aaabbbc"
    string2 = "bbccde"
    assert create_strings_from_characters(frequencies, string1, string2) == 2

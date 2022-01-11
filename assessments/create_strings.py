"""
https://www.programmingexpert.io/programming-fundamentals/assessment/6
"""


def create_strings_from_characters(frequencies, string1, string2):
    string1_val = is_valid(frequencies, string1)
    string2_val = is_valid(frequencies, string2)

    if string1_val and string2_val:
        return 2
    elif string1_val or string2_val:
        return 1
    else:
        return 0


def is_valid(frequencies, string):
    valid_string = 1
    prev = ""
    for letter in string:
        count = string.count(letter)
        if letter == prev:
            continue
        elif (
            letter not in frequencies
            or frequencies[letter] < count
            or frequencies[letter] == 0
        ):
            valid_string = 0
            break

        frequencies[letter] -= count
        prev = letter
    return valid_string

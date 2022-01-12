"""
https://www.programmingexpert.io/programming-fundamentals/assessment/6
"""

# Sol 1
def create_strings_from_characters(frequencies, string1, string2):
    can_create_string1 = is_valid_string(frequencies, string1)
    can_create_string2 = is_valid_string(frequencies, string2)

    if can_create_string1 and can_create_string2:
        return 2
    elif can_create_string1 or can_create_string2:
        return 1
    return 0


def is_valid_string(frequencies, string):
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


# Sol 2
def create_strings_from_characters(frequencies, string1, string2):
    can_create_string1 = is_valid_string(frequencies, string1)
    can_create_string2 = is_valid_string(frequencies, string2)

    if can_create_string1 and can_create_string2:
        return 2
    elif can_create_string1 or can_create_string2:
        return 1
    return 0


def is_valid_string(frequencies, string):
    for letter in set(string):
        if (
            letter not in frequencies
            or string.count(letter) > frequencies[letter]
            or frequencies[letter] == 0
        ):
            return 0
        frequencies[letter] -= string.count(letter)
    return 1


# Sol 3
def create_strings_from_characters(frequencies, string1, string2):
    can_create_string1 = is_valid_string(frequencies, string1)
    can_create_string2 = is_valid_string(frequencies, string2)

    if can_create_string1 and can_create_string2:
        return 2
    elif can_create_string1 or can_create_string2:
        return 1
    return 0


def is_valid_string(frequencies, string):
    for letter in set(string):
        if string.count(letter) > frequencies.get(letter, 0):
            return False
        frequencies[letter] -= string.count(letter)
    return True

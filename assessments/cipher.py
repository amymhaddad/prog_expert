"""
https://www.programmingexpert.io/programming-fundamentals/assessment/2
"""

from string import ascii_lowercase as lower 

ALPHA_LENGTH = 26

def caesar_cipher(string, offset):
    
    new_word = ""
    letter_indexes = {i: letter for i, letter in enumerate(lower)} 
    
    for char in string:
        index = ord(char) - ord("a")
        letter_index = letter_indexes[index]
        new_char = (index - offset) % 26
        new_word += letter_indexes[new_char]
    return new_word

#print(caesar_cipher("apple", 5))

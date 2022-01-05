"""
https://www.programmingexpert.io/programming-fundamentals/assessment/2
"""
#Sol 1
from string import ascii_lowercase as lower 

ALPHA_LENGTH = 26

def caesar_cipher(string, offset):  
    new_word = []
    letter_indexes = {i: letter for i, letter in enumerate(lower)} 
    
    for char in string:
        dist = ord(char) - ord("a")
        index = (dist - offset) % 26
        new_word.append(letter_indexes[index])
    return "".join(new_word)

#Sol 2 
def caesar_cipher(string, offset):
    
    new_word = []
    alpha  =["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    
    for char in string:
        curr_index = alpha.index(char)
        index = curr_index - offset 
        new_word.append(alpha[index])
    return "".join(new_word)

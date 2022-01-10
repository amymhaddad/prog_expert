"""
https://www.programmingexpert.io/programming-fundamentals/assessment/6
"""

def create_strings_from_characters(frequencies, string1, string2):

   # import pdb; pdb.set_trace()
    string1_val = is_valid(frequencies, string1) 
    string2_val = is_valid(frequencies, string2)

    
    print(string1_val, string2_val)



def is_valid(frequencies, string):

    first_string = None
    for letter in string:
        count = string.count(letter)
        
        if letter not in frequencies or frequencies[letter] < count:
            first_string = 0 
        else:
            frequencies[letter] -= count 

    if first_string:
        first_string = 1

    return first_string
frequencies = {"h": 2, "e": 1, "l": 1, "r": 4, "a": 3, "o": 2, "d": 1, "w": 1}
string1 = "hello"
string2 = "world"
print(create_strings_from_characters(frequencies, string1, string2))

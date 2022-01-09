"""
https://www.programmingexpert.io/programming-fundamentals/assessment/4
"""


def get_n_longest_unique_words(words, n):
    unique_words = get_unique_words(words)
    sorted_words = sorted(unique_words.items(), key=lambda x: x[1], reverse=True)

    return [word[0] for word in sorted_words[:n]]


def get_unique_words(words):

    unique_words = {}

    for word in words:
        if word in unique_words:
            unique_words.pop(word)
        else:
            unique_words[word] = len(word)
    return unique_words

words = ["Longer", "Whatever", "Longer", "Ball", "Rock", "Rocky", "Rocky"]
print(get_n_longest_unique_words(words, 3))

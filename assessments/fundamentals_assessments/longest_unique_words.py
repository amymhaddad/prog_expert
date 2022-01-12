"""
https://www.programmingexpert.io/programming-fundamentals/assessment/4
"""

words = ["Longer", "Whatever", "Longer", "Ball", "Rock", "Rocky", "Rocky"]

# Sol 1
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


# Sol 2
def get_n_longest_unique_words(words, n):
    words = get_unique_words(words)
    longest_words = []

    while len(longest_words) < n:
        current_longest = ""
        for word in words:
            if len(word) > len(current_longest):
                current_longest = word
        longest_words.append(current_longest)
        words.remove(current_longest)

    return longest_words


def get_unique_words(words):

    return [word for word in words if words.count(word) == 1]


# Sol 3


def get_n_longest_unique_words(words, n):
    unique_words = get_unique_words(words)
    sorted_words = sorted(unique_words, key=len, reverse=True)
    return sorted_words[:n]


def get_unique_words(words):

    return [word for word in words if words.count(word) == 1]

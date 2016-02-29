import string


def is_pangram(sentence):
    sentence = sentence.lower()

    return set(string.ascii_lowercase).issubset(set(sentence))
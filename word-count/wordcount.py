# -*- coding: utf-8 -*-
import re


def word_count(sentence):
    counted_words = dict()
    clean_sentence = re.sub(r'[^а-яА-ЯA-Za-z0-9]', ' ', sentence)
    words = clean_sentence.lower().split()

    for word in words:
        counted_words[word.decode('utf-8', errors='ignore')] = words.count(word)

    return counted_words


print(word_count('до свидание'))


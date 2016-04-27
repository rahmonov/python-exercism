def translate(words):
    pigged_list = list()

    for word in words.split():
        pigged_list.append(piggify(word))

    return ' '.join(pigged_list)


def piggify(word):
    result = get_edge_case(word)

    if not result:
        result = get_regular(word)

    return result


def get_edge_case(word):
    result = None

    if (word[0] == 'y' and is_vowel(word[1])) or (word[0] == 'x' and is_vowel(word[1])):
        result = word[1:] + word[0] + 'ay'

    if word[:2] == 'ch' or word[:2] == 'qu' or word[:2] == 'th':
        result = word[2:] + word[:2] + 'ay'

    if word[:3] == 'squ' or word[:3] == 'sch' or word[:3] == 'thr':
        result = word[3:] + word[:3] + 'ay'

    return result


def get_regular(word):
    if is_vowel(word[0]):
        return word + 'ay'

    return word[1:] + word[0] + 'ay'


def is_vowel(character):
    if character.lower() in 'aeoiuyx':
        return True

    return False

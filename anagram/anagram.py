def detect_anagrams(original, words):
    return [word for word in words if is_anagram(original, word)]


def is_anagram(original, version):
    original, version = map(lambda x: x.lower(), [original, version])
    return sorted(original) == sorted(version) and original != version
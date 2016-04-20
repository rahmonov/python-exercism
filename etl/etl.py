def transform(old):
    return {word.lower(): score for score in old for word in old[score]}

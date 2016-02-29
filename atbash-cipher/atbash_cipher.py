from string import maketrans, ascii_letters

trantab = maketrans(ascii_letters, ascii_letters.lower()[::-1])


def decode(text):
    return ''.join(char for char in text if char.isalnum()).translate(trantab)


def encode(text):
    text = decode(text)
    return ' '.join(text[i:i+5] for i in range(0, len(text), 5))



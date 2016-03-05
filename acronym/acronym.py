import re


def abbreviate(text):
    acronym = ''
    words = re.split('[ -]', text)

    for word in words:
        acronym += word[0].upper()
        acronym += ''.join([char for char in re.findall('(?<=[a-z])([A-Z])', word)])

    return acronym


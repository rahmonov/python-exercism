# -*- coding: utf-8 -*-


def encode(input):
    current = input[0]
    count = 0
    result = ''

    for index, char in enumerate(input):
        if current == char:
            count += 1
        else:
            if count == 1:
                result += current
            else:
                result += str(count) + current
            current = char
            count = 1

    if count == 1:
        result += current
    else:
        result += str(count) + current

    return result


def decode(input):
    result = ''
    count = ''

    for index, char in enumerate(input):
        if char.isdigit():
            count += char
        else:
            if count:
                result += int(count) * char
            else:
                result += char
            count = ''

    return result

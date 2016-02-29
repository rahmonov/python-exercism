def slices(number, length):
    if len(number) < length or length == 0:
        raise ValueError("Length should be shorter than the length of the number")

    result = []
    for i in range(len(number) - length + 1):
        result.append(map(int, list(number[i:i+length])))

    return result



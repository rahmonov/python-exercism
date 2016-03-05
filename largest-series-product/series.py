

def largest_product(str_number, length):
    if length == 0:
        return 1

    return max(map(lambda l: reduce(lambda x, y: x * y, l), slices(str_number, length)))


def slices(str_number, length):
    if length > len(str_number):
        raise ValueError("Wrong input of length parameter")

    return [map(int, list(str_number[index:index+length])) for index in range(0, len(str_number) - length + 1)]

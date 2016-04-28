SUBLIST, SUPERLIST, EQUAL, UNEQUAL = 1, 2, 3, 4


def check_lists(a, b):
    if len(a) < len(b) and is_sublist(a, b):
        return SUBLIST
    elif len(a) > len(b) and is_sublist(b, a):
        return SUPERLIST
    elif a == b:
        return EQUAL
    else:
        return UNEQUAL


def is_sublist(a, b):
    for val in range(len(b) - len(a) + 1):
        if b[val:val+len(a)] == a:
            return True
    return False


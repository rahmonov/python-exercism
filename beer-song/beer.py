def verse(nth):
    if nth > 1:
        v = "{0} bottles of beer on the wall, {0} bottles of beer.\n"\
            "Take one down and pass it around, "\
            "{1} {2} of beer on the wall.\n".format(
            nth, nth-1, "bottles" if nth > 2 else "bottle")
    elif nth == 1:
        v = "{0} bottle of beer on the wall, {0} bottle of beer.\n"\
            "Take it down and pass it around, "\
            "no more bottles of beer on the wall.\n".format(nth)
    else:
        v = "No more bottles of beer on the wall, no more bottles of beer.\n"\
            "Go to the store and buy some more, "\
            "99 bottles of beer on the wall.\n"\

    return v


def song(_from, _to=0):
    result = ''

    for i in range(_from, _to-1, -1):
        result += verse(i) + '\n'

    return result

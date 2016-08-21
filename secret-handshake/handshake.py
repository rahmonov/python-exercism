MASKS = {
    'wink': 0b1,
    'double blink': 0b10,
    'close your eyes': 0b100,
    'jump': 0b1000,
}

MASK_NAMES = ['wink', 'double blink', 'close your eyes', 'jump']

REVERSE_MASK = 0b10000


def code(operations):
    result = 0b00000
    reversed_ = False

    if not set(operations).issubset(set(MASK_NAMES)):
        return '0'

    for ind, op in enumerate(operations):
        result ^= MASKS[op]

        if ind != len(operations) - 1 and not reversed_ and MASKS[op] > MASKS[operations[ind + 1]]:
            result ^= REVERSE_MASK
            reversed_ = True

    return bin(result)[2:]


def handshake(decimal):
    if isinstance(decimal, int) and decimal < 0:
        return []

    if isinstance(decimal, str):
        if not set(decimal).issubset({'1', '0'}):
            return []

        decimal = int(decimal, 2)

    operations = list()

    for mask in MASK_NAMES:
        is_on = MASKS[mask] & decimal

        if is_on:
            operations.append(mask)

    if REVERSE_MASK & decimal:
        operations.reverse()

    return operations

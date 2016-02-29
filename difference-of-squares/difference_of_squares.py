def square_of_sum(nth):
    return sum(range(1, nth+1)) ** 2


def sum_of_squares(nth):
    return sum(map(lambda x: x ** 2, range(1, nth+1)))


def difference(nth):
    return square_of_sum(nth) - sum_of_squares(nth)


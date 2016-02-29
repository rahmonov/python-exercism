def sum_of_multiples(number, factors=[3, 5]):
    """
    Calculates the sum of multiples of factors up to the number.
    """
    return sum([n for n in range(0, number) if divides_by(n, factors)])


def divides_by(number, numbers):
    """
    Checks if number can be equally divided by any of numbers.
    """
    return any(number % n == 0 for n in numbers if n != 0)
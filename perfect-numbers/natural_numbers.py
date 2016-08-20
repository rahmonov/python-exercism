def factors_generator(number):
    yield 1
    for i in range(2, int(number ** 0.5 + 1)):
            if number % i == 0:
                    yield i
                    yield number / i


def is_perfect(number):
    return sum(factors_generator(number)) == number

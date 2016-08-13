from math import sqrt


def is_prime(test):
    if test == 2:
        return True
    
    if test < 2 or test % 2 == 0:
        return False

    return not any(test % i == 0 for i in range(3, int(sqrt(test)) + 1, 2))


def nth_prime(n):
    test_num = 2
    prime_count = 1

    while prime_count < n:
        test_num += 1

        if is_prime(test_num):
            prime_count += 1

    return test_num

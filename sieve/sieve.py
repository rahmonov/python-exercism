def sieve(nth):
    primality_list = [True] * (nth+1)
    primality_list[0] = primality_list[1] = False

    for index, is_prime in enumerate(primality_list):
        if is_prime:
            for j in range(index*index, nth+1, index):
                primality_list[j] = False

    return [index for index, val in enumerate(primality_list) if val]


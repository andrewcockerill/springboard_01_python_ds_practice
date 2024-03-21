def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    prime_factors = []
    n = num

    while n % 2 == 0:
        prime_factors = prime_factors + [2]
        n = n // 2

    for i in range(3, int(n**0.5)+1, 2):
        while n % i == 0:
            prime_factors += [i]
            n = n // i

    if n > 2:
        prime_factors += [n]

    prime_combos = [prime_factors[i:j] for i in range(
        len(prime_factors)) for j in range(i+1, len(prime_factors)+1)]

    all_factors = []

    def multiply_nums(lst):
        if len(lst) == 0:
            return 1
        else:
            return lst[0] * multiply_nums(lst[1:])

    all_factors = sorted(
        list(set([1]+[multiply_nums(i) for i in prime_combos])))

    return all_factors


find_factors(10)
find_factors(11)
find_factors(111)
find_factors(321421)
find_factors(321421993)

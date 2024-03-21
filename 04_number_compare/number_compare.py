def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a

        >>> number_compare(1, 1)
        'Numbers are equal'

        >>> number_compare(-1, 1)
        'Second is greater'

        >>> number_compare(1, -2)
        'First is greater'
    """
    a_ge_b = (a >= b)*1
    b_ge_a = (b >= a)*-1
    score = a_ge_b + b_ge_a
    results_dict = {-1: 'Second is greater',
                    0: 'Numbers are equal', 1: 'First is greater'}
    return results_dict[score]


number_compare(1, 1)
number_compare(-1, 1)
number_compare(1, -2)

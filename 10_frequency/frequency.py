def frequency(lst, search_term):
    """Return frequency of term in lst.

        >>> frequency([1, 4, 3, 4, 4], 4)
        3

        >>> frequency([1, 4, 3], 7)
        0
    """
    match_list = [i == search_term for i in lst]
    return sum(match_list)


frequency([1, 4, 3, 4, 4], 4)
frequency([1, 4, 3], 7)

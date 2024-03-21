def last_element(lst):
    """Return last item in list (None if list is empty.

        >>> last_element([1, 2, 3])
        3

        >>> last_element([]) is None
        True
    """
    len_lst = len(lst)
    if len_lst == 0:
        return None
    else:
        return lst[-1]


last_element([1, 2, 3])
last_element([]) is None

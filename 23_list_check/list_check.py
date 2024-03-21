def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    checks = [isinstance(i, list) for i in lst]
    return all(checks)


list_check([[1], [2, 3]])
list_check([[1], "nope"])

def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """
    idx_start = 0
    has_indices = type(collection) in [list, tuple, str]
    result = False

    if has_indices:
        start_idx = int(start or 0)
        result = sought in collection[start:]
    else:
        if isinstance(collection, set):
            result = sought in collection
        else:
            result = sought in collection.values()
    return result


includes([1, 2, 3], 1)
includes([1, 2, 3], 1, 2)
includes("hello", "o")
includes(('Elmo', 5, 'red'), 'red', 1)
includes({1, 2, 3}, 1)
includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
includes({"apple": "red", "berry": "blue"}, "blue")

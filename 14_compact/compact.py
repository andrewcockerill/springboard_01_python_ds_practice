def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    return [i for i in lst if i]


compact([0, 1, 2, '', [], False, (), None, 'All done'])

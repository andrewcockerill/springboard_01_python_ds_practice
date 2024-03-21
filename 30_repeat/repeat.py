def repeat(phrase, num):
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """
    result = None
    if isinstance(num, int):
        if num >= 0:
            result = phrase*num
    return result


repeat('*', 3)
repeat('abc', 2)
repeat('abc', 0)
repeat('abc', -1) is None
repeat('abc', 'nope') is None

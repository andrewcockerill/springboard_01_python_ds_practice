def truncate(phrase, n):
    """Return truncated-at-n-chars version of  phrase.

    If the phrase is longer than, or the same size as, n make sure it ends with '...' and is no
    longer than n.

        >>> truncate("Hello World", 6)
        'Hel...'

        >>> truncate("Problem solving is the best!", 10)
        'Problem...'

        >>> truncate("Yo", 100)
        'Yo'

    The smallest legal value of n is 3; if less, return a message:

        >>> truncate('Cool', 1)
        'Truncation must be at least 3 characters.'

        >>> truncate("Woah", 4)
        'W...'

        >>> truncate("Woah", 3)
        '...'
    """
    result = 'Truncation must be at least 3 characters.'
    if n >= 3:
        len_phrase = len(phrase)
        result = phrase[:]
        if len_phrase >= n:
            result = phrase[0:n-3] + '...'

    return result


truncate("Hello World", 6)
truncate("Problem solving is the best!", 10)
truncate("Yo", 100)
truncate('Cool', 1)
truncate("Woah", 4)
truncate("Woah", 3)

def intersection(l1, l2):
    """Return intersection of two lists as a new list::

        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]

        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]

        >>> intersection([1, 2, 3], [3, 4])
        [3]

        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """

    l1_unique = list(set(l1))
    l2_unique = list(set(l2))
    combined = l1_unique + l2_unique
    val_counts = {k: 0 for k in list(set(combined))}
    for i in combined:
        val_counts[i] += 1
    return [i for i, j in val_counts.items() if j > 1]


intersection([1, 2, 3], [2, 3, 4])
intersection([1, 2, 3], [1, 2, 3, 4])
intersection([1, 2, 3], [3, 4])
intersection([1, 2, 3], [4, 5, 6])

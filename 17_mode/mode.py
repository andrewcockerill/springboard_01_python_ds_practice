def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    vals = list(set(nums))
    val_counts = {k: 0 for k in vals}
    incumbent = nums[0]
    incumbent_count = 0
    for n in nums:
        val_counts[n] += 1
        if val_counts[n] > incumbent_count:
            incumbent_count = val_counts[n]
            incumbent = n
    return incumbent


mode([1, 2, 1])
mode([2, 2, 3, 3, 2])

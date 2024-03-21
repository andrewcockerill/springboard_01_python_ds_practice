def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    idx_dict = {}
    for i, j in enumerate(nums):
        if bool(idx_dict.get(j)):
            idx_dict[j] += [i]
        else:
            idx_dict[j] = [i]

    incumbent = ()
    incumbent_idx = len(nums)

    for i, j in enumerate(nums):
        compliment = goal - j
        compliment_indices = idx_dict.get(compliment)
        if compliment_indices is not None:
            compliment_indices = [k for k in compliment_indices if k != i]
        if compliment_indices:
            goal_met_index = max(min(compliment_indices), i)
            if (not bool(incumbent)) | (bool(incumbent) & (incumbent_idx > goal_met_index)):
                incumbent_idx = goal_met_index
                incumbent = (j, compliment)

    return incumbent


sum_pairs([1, 2, 2, 10], 4)
sum_pairs([4, 2, 10, 5, 1], 6)
sum_pairs([5, 1, 4, 8, 3, 2], 7)
sum_pairs([11, 20, 4, 2, 1, 5], 100)

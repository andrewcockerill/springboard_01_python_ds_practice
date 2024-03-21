def sum_floats(nums):
    """Return sum of floating point numbers in nums.

        >>> sum_floats([1.5, 2.4, 'awesome', [], 1])
        3.9

        >>> sum_floats([1, 2, 3])
        0
    """

    # hint: to find out if something is a float, you should use the
    # "isinstance" function --- research how to use this to find out
    # if something is a float!

    if not nums:
        return 0
    else:
        for n in nums:
            if isinstance(n, float):
                return n + sum_floats(nums[1:])
            else:
                return 0 + sum_floats(nums[1:])


sum_floats([1.5, 2.4, 'awesome', [], 1])
sum_floats([1, 2, 3])

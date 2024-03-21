def multiply_even_numbers(nums):
    """Multiply the even numbers.

        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48

        >>> multiply_even_numbers([3, 4, 5])
        4

    If there are no even numbers, return 1.

        >>> multiply_even_numbers([1, 3, 5])
        1
    """
    if len(nums) == 0:
        return 1
    elif nums[0] % 2 == 0:
        return nums[0] * multiply_even_numbers(nums[1:])
    else:
        return 1 * multiply_even_numbers(nums[1:])


multiply_even_numbers([2, 3, 4, 5, 6])
multiply_even_numbers([3, 4, 5])
multiply_even_numbers([1, 3, 5])

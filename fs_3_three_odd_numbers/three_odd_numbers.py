def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """

    for i in range(len(nums)-3+1):
        three_seq = nums[i:i+3]
        add_three = sum(three_seq)
        if add_three % 2 != 0:
            return True
    return False


three_odd_numbers([1, 2, 3, 4, 5])
three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
three_odd_numbers([5, 2, 1])
three_odd_numbers([1, 2, 3, 3, 2])

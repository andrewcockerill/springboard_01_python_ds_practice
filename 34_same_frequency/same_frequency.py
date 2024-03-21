def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

        >>> same_frequency(551122, 221515)
        True

        >>> same_frequency(321142, 3212215)
        False

        >>> same_frequency(1212, 2211)
        True
    """
    num1_freqs = {str(k): 0 for k in range(10)}
    num2_freqs = {str(k): 0 for k in range(10)}
    num1_str = str(num1)
    num2_str = str(num2)

    for c in num1_str:
        num1_freqs[c] += 1
    for c in num2_str:
        num2_freqs[c] += 1

    return num1_freqs == num2_freqs


same_frequency(551122, 221515)
same_frequency(321142, 3212215)
same_frequency(1212, 2211)

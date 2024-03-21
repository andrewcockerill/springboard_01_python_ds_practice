def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    n = len(matrix[0])

    tl_br_sum = 0
    bl_tr_sum = 0

    i = 0
    j = 0

    while (i != n) & (j != n):
        tl_br_sum += matrix[i][j]
        i += 1
        j += 1

    i = n-1
    j = 0

    while (i != -1) & (j != n):
        tl_br_sum += matrix[i][j]
        i -= 1
        j += 1

    return tl_br_sum + bl_tr_sum


m1 = [
    [1,   2],
    [30, 40]
]

sum_up_diagonals(m1)
m2 = [
     [1, 2, 3],
     [4, 5, 6],
     [7, 8, 9],
]
sum_up_diagonals(m2)

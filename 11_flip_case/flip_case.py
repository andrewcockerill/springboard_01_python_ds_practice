def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    input_lower = to_swap.lower()
    ord_num = ord(input_lower)

    result = [c if c.lower() != input_lower else (
        c.lower() if ord(c) < 91 else c.upper()) for c in phrase]
    return ''.join(result)


flip_case('Aaaahhh', 'a')
flip_case('Aaaahhh', 'A')
flip_case('Aaaahhh', 'h')

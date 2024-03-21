def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    # Setup count dictionary
    letters_lower = [chr(i) for i in range(ord('a'), ord('z')+1)]
    letters_upper = [i.upper() for i in letters_lower]
    letters_all = letters_lower + letters_upper
    letters_dict = {c: 0 for c in letters_all}

    # Tabulate
    for c in phrase:
        letters_dict[c] += 1

    return {k: v for k, v in letters_dict.items() if v > 0}


multiple_letter_count('yay')
multiple_letter_count('Yay')

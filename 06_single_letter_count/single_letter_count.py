def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?

        >>> single_letter_count('Hello World', 'h')
        1

        >>> single_letter_count('Hello World', 'z')
        0

        >>> single_letter_count("Hello World", 'l')
        3
    """
    word_lower = word.lower()
    letter_count = 0
    for c in word_lower:
        if c == letter:
            letter_count += 1

    return letter_count


single_letter_count('Hello World', 'h')
single_letter_count('Hello World', 'z')
single_letter_count('Hello World', 'l')

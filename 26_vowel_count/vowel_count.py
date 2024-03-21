def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}

        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    vowel_dict = {k: 0 for k in ['a', 'e', 'i', 'o', 'u']}
    phrase_lower = phrase.lower()
    for c in phrase_lower:
        if vowel_dict.get(c) is not None:
            vowel_dict[c] += 1
    return {k: v for k, v in vowel_dict.items() if v > 0}


vowel_count('rithm school')
vowel_count('HOW ARE YOU? i am great!')

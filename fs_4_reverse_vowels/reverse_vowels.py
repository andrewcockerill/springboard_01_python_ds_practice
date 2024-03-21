def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vowel_locs = {}
    for i, j in enumerate(s):
        if j in vowels:
            vowel_locs[i] = j
    locs_ordered = sorted(list(vowel_locs.keys()))
    vals_ordered = [vowel_locs[i] for i in locs_ordered]
    vals_reversed = vals_ordered[::-1]
    new_vowel_locs = {k: v for k, v in zip(locs_ordered, vals_reversed)}
    new_word = [i for i in s]
    for k in new_vowel_locs.keys():
        new_word[k] = new_vowel_locs[k]
    return ''.join(new_word)


reverse_vowels("Hello!")
reverse_vowels("Tomatoes")
reverse_vowels("Reverse Vowels In A String")
reverse_vowels("aeiou")
reverse_vowels("why try, shy fly?")

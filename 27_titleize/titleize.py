def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    split_phrase = phrase.split()
    title_list = [i.lower() for i in split_phrase]
    title_list = [i[0].upper()+i[1:] for i in title_list]
    return ' '.join(title_list)


titleize('this is awesome')
titleize('oNLy cAPITALIZe fIRSt')

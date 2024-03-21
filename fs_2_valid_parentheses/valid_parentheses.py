def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    score_num = 0
    for p in parens:
        if p == '(':
            score_num += 1
        else:
            score_num -= 1
        if score_num < 0:
            return False
    if score_num == 0:
        return True
    else:
        return False


valid_parentheses("()")
valid_parentheses("()()")
valid_parentheses("(()())")
valid_parentheses(")()")
valid_parentheses("())")
valid_parentheses("((())")
valid_parentheses(")()(")

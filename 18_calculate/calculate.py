def calculate(operation, a, b, make_int=False, message='The result is'):
    """Perform operation on a + b, ()possibly truncating) & returning w/msg.

    - operation: 'add', 'subtract', 'multiply', or 'divide'
    - a and b: values to operate on
    - make_int: (optional, defaults to False) if True, truncates to integer
    - message: (optional) message to use (if not provided, use 'The result is')

    Performs math operation (truncating if make_int), then returns as
    "[message] [result]"

        >>> calculate('add', 2.5, 4)
        'The result is 6.5'

        >>> calculate('subtract', 4, 1.5, make_int=True)
        'The result is 2'

        >>> calculate('multiply', 1.5, 2)
        'The result is 3.0'

        >>> calculate('divide', 10, 4, message='I got')
        'I got 2.5'

    If a valid operation isn't provided, return None.

        >>> calculate('foo', 2, 3)

    """
    string_ops = {
        'add': lambda x, y: x+y,
        'subtract': lambda x, y: x-y,
        'multiply': lambda x, y: x*y,
        'divide': lambda x, y: x/y
    }

    if operation in string_ops.keys():
        res = string_ops[operation](a, b)
        if make_int:
            res = int(res)
        return f'{message} {res}'
    else:
        return None


calculate('add', 2.5, 4)
calculate('subtract', 4, 1.5, make_int=True)
calculate('multiply', 1.5, 2)
calculate('divide', 10, 4, message='I got')
calculate('foo', 2, 3)

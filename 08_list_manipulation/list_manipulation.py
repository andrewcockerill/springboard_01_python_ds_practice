def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """

    valid_input = (command in ['add', 'remove']) & (
        location in ['beginning', 'end'])
    return_val = None
    lst_arg = lst[:]
    if valid_input:
        if command == 'add':
            if location == 'beginning':
                lst[:] = [value] + lst_arg
            else:
                lst[:] = lst_arg + [value]
            return_val = lst
        else:
            if location == 'beginning':
                return_val = lst_arg[0]
                lst[:] = lst_arg[1:]
            else:
                return_val = lst_arg[-1]
                lst[:] = lst_arg[:-1]
    return return_val


# Testing
print('\n Test 1:')
lst = [1, 2, 3]
list_manipulation(lst, 'remove', 'end')
list_manipulation(lst, 'remove', 'beginning')
lst
print('\n Test 2:')
lst = [1, 2, 3]
list_manipulation(lst, 'add', 'beginning', 20)
list_manipulation(lst, 'add', 'end', 30)
lst
print('\n Test 3:')
list_manipulation(lst, 'foo', 'end') is None
list_manipulation(lst, 'add', 'dunno') is None

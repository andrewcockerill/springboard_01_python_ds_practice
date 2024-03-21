def weekday_name(day_of_week):
    """Return name of weekday.

        >>> weekday_name(1)
        'Sunday'

        >>> weekday_name(7)
        'Saturday'

    For days not between 1 and 7, return None

        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    day_nums = [i for i in range(1, 8)]
    day_names = ['Sunday', 'Monday', 'Tuesday',
                 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    day_dict = dict(zip(day_nums, day_names))

    if day_of_week in day_nums:
        return day_dict[day_of_week]
    else:
        return None


weekday_name(1)
weekday_name(7)
weekday_name(8)

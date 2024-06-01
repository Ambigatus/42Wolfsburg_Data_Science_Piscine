def ft_filter(function, iterable):
    """
    ft_filter takes two parameters - function of None and iterable. Then, filter that object

    :param function: function or None
    :param iterable: something iterable
    :return: Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true.

    print(filter.__doc__)
    """

    if function is None:
        return (item for item in iterable if item)
    else:
        return (item for item in iterable if function(item))

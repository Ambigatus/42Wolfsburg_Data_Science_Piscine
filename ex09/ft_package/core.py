def count_in_list(lst, item):
    """
    Count occurrences of an item in a list.
    :param lst: List of items
    :param item: Item to count
    :return: Count of item in the list
    """
    count = 0
    for element in lst:
        if element == item:
            count += 1
    return count

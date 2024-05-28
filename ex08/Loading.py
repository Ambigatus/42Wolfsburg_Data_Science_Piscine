def ft_tqdm(lst: range) -> None:
    """
    Prototype function, which mimics tqdm's progress bar
    :param lst: Elements
    :return: Progress bar
    """

    # Counter for elements in lst
    elements = 0
    for _ in lst:
        elements += 1

    progress_bar = 40  # Length of bar

    i = 0
    for elem in lst:
        i += 1
        progress = (i * 100) // elements  # Procent to finish
        block = (progress * progress_bar) // 100  # Number of blocks in progress bar

        # Creating progress bar manually
        bar = '['
        j = 0
        while j < progress_bar:
            if j < block:
                bar += "="
            elif j == block:
                bar += '>'
            else:
                bar += ' '
            j += 1
        bar += ']'

        percentage = str(progress) + "%"
        progress_str = str(i) + "/" + str(elements)
        text = percentage + " " + bar + " " + progress_str
        print("\r" + text, end='', flush=True)

# The yield keyword in Python allows a function to produce a series of values over time, returning each value one
# at a time. In the ft_tqdm function, yield elem is used to yield each element from the input range, allowing the
# function to generate progress updates as it iterates over the range.
        yield elem

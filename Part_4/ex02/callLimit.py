def callLimit(limit: int):
    """
    A decorator function that restricts the number of times a given function can be called.

    :param limit: Maximum number of allowed calls to the function.
    :return: A wrapper function that limits the number of calls.
    """

    def callLimiter(function):
        count = 0

        def limit_function(*args, **kwargs):
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwargs)
            else:
                print(f"Error: {function} call too many times")

        return limit_function

    return callLimiter

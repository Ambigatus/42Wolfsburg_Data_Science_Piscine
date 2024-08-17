def square(x: int | float) -> int | float:
    """
    Returns the square of the given number.

    Args:
        x (int or float): The number to square.

    Returns:
        int or float: The square of the number.
    """
    return x ** 2


def pow(x: int | float) -> int | float:
    """
    Returns the result of exponentiating the given number by itself.

    Args:
        x (int or float): The number to exponentiate.

    Returns:
        int or float: The result of x raised to the power of x.
    """
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Takes a number and a function as arguments, returning an object that
    when called, returns the result of repeatedly applying the function
    to the result of the previous call.

    Args:
        x (int or float): The initial number.
        function (callable): The function to apply.

    Returns:
        object: A callable object that returns the result of the function
        applied to the number each time it's called.
    """
    count = 0

    def inner() -> float:
        nonlocal count
        count += 1
        result = x
        for _ in range(count):
            result = function(result)
        return result

    return inner


def main():
    """
    Main function to execute test cases for the in_out functions.
    The function is not executed if the script is run directly.
    """
    pass


if __name__ == "__main__":
    main()

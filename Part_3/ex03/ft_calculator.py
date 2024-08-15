class calculator:
    def __init__(self, vector):
        """
        Initializes the calculator with a vector.

        :param vector: A list of floats representing the vector.
        """
        self.vector = vector

    def __add__(self, scalar):
        """
        Adds a scalar to each element of the vector.

        :param scalar: A float or int to be added to each element of the vector.
        :return: None, but prints the result of the addition.
        """
        result = [x + scalar for x in self.vector]
        print(result)

    def __mul__(self, scalar):
        """
        Multiplies each element of the vector by a scalar.

        :param scalar: A float or int to multiply each element of the vector.
        :return: None, but prints the result of the multiplication.
        """
        result = [x * scalar for x in self.vector]
        print(result)

    def __sub__(self, scalar):
        """
        Subtracts a scalar from each element of the vector.

        :param scalar: A float or int to subtract from each element of the vector.
        :return: None, but prints the result of the subtraction.
        """
        result = [x - scalar for x in self.vector]
        print(result)

    def __truediv__(self, scalar):
        """
        Divides each element of the vector by a scalar.
        Raises ZeroDivisionError if scalar is 0.

        :param scalar: A float or int to divide each element of the vector.
        :return: None, but prints the result of the division.
        """
        if scalar == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        result = [x / scalar for x in self.vector]
        print(result)

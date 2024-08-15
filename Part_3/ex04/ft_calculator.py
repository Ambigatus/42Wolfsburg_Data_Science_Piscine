class calculator:
    """
    A calculator class for performing operations (dot product, addition, subtraction)
    on two vectors.
    """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Computes and prints the dot product of two vectors.

        :param V1: First vector (list of floats)
        :param V2: Second vector (list of floats)
        :return: None, but prints the result of the dot product.
        """
        result = sum(float(x) * float(y) for x, y in zip(V1, V2))
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Adds two vectors and prints the result.

        :param V1: First vector (list of floats)
        :param V2: Second vector (list of floats)
        :return: None, but prints the result of the vector addition.
        """
        result = [float(x) + float(y) for x, y in zip(V1, V2)]
        print(f"Add Vector is : {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Subtracts the second vector from the first and prints the result.

        :param V1: First vector (list of floats)
        :param V2: Second vector (list of floats)
        :return: None, but prints the result of the vector subtraction.
        """
        result = [float(x) - float(y) for x, y in zip(V1, V2)]
        print(f"Sous Vector is: {result}")

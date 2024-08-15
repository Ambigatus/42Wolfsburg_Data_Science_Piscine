from S1E9 import Character


class Baratheon(Character):
    """
    Representing the Baratheon family.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Constructor for the Baratheon class.

        Parameters:
        -----------
        first_name : str
            The first name of the Baratheon character.
        is_alive : bool, optional
            A boolean flag indicating whether the Baratheon character is alive. Default is True.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """
        Method to change the Baratheon character's alive status to False.
        """
        self.is_alive = False

    def __str__(self):
        """
        Return a string representation of the Baratheon character.
        """
        return f"<bound method Baratheon.__str__ of Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')>"

    def __repr__(self):
        """
        Return a string representation of the Baratheon character for debugging.
        """
        return f"<bound method Baratheon.__repr__ of Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')>"

    @classmethod
    def create_baratheon(cls, first_name, is_alive=True):
        """
        Class method to create a Baratheon character.

        Parameters:
        -----------
        first_name : str
            The first name of the Baratheon character.
        is_alive : bool, optional
            A boolean flag indicating whether the Baratheon character is alive. Default is True.

        Returns:
        --------
        Baratheon
            An instance of the Baratheon class.
        """
        return cls(first_name, is_alive)


class Lannister(Character):
    """
    Representing the Lannister family.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Constructor for the Lannister class.

        Parameters:
        -----------
        first_name : str
            The first name of the Lannister character.
        is_alive : bool, optional
            A boolean flag indicating whether the Lannister character is alive. Default is True.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """
        Method to change the Lannister character's alive status to False.
        """
        self.is_alive = False

    def __str__(self):
        """
        Return a string representation of the Lannister character.
        """
        return f"<bound method Lannister.__str__ of Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')>"

    def __repr__(self):
        """
        Return a string representation of the Lannister character for debugging.
        """
        return f"<bound method Lannister.__repr__ of Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')>"

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """
        Class method to create a Lannister character.

        Parameters:
        -----------
        first_name : str
            The first name of the Lannister character.
        is_alive : bool, optional
            A boolean flag indicating whether the Lannister character is alive. Default is True.

        Returns:
        --------
        Lannister
            An instance of the Lannister class.
        """
        return cls(first_name, is_alive)


def main():
    """
    Main function to test Baratheon and Lannister classes.
    """

    # Creating Baratheon characters
    Robert = Baratheon("Robert")
    print(Robert.__dict__)
    print(Robert.__str__)
    print(Robert.__repr__)
    print(Robert.is_alive)
    Robert.die()
    print(Robert.is_alive)
    print(Robert.__doc__)
    print("---")

    # Creating Lannister characters
    Cersei = Lannister("Cersei")
    print(Cersei.__dict__)
    print(Cersei.__str__)
    print(Cersei.is_alive)
    print("---")

    # Using the class method to create a Lannister character
    Jaine = Lannister.create_lannister("Jaine", True)
    print(f"Name : ({Jaine.first_name}, {type(Jaine).__name__}), Alive : {Jaine.is_alive}")


if __name__ == "__main__":
    main()

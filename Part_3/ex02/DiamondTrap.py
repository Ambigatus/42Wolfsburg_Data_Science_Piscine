from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
    """
    Represents a King, specifically Joffrey Baratheon, who inherits traits from both
    Baratheon and Lannister families.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Constructor for the King class.

        Parameters:
        -----------
        first_name : str
            The first name of the King character.
        is_alive : bool, optional
            A boolean flag indicating whether the King character is alive. Default is True.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"  # Default Baratheon traits
        self.hairs = "dark"

    def get_eyes(self):
        """
        Returns the color of the King's eyes.
        """
        return self.eyes

    def set_eyes(self, color: str):
        """
        Sets the color of the King's eyes.

        Parameters:
        -----------
        color : str
            The new color of the King's eyes.
        """
        self.eyes = color

    def get_hairs(self):
        """
        Returns the color of the King's hair.
        """
        return self.hairs

    def set_hairs(self, color: str):
        """
        Sets the color of the King's hair.

        Parameters:
        -----------
        color : str
            The new color of the King's hair.
        """
        self.hairs = color


def main():
    """
    Main function to test the King class.
    """

    Joffrey = King("Joffrey")
    print(Joffrey.__dict__)
    Joffrey.set_eyes("blue")
    Joffrey.set_hairs("light")
    print(Joffrey.get_eyes())
    print(Joffrey.get_hairs())
    print(Joffrey.__dict__)

if __name__ == "__main__":
    main()

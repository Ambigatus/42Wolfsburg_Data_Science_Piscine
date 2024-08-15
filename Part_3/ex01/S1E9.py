from abc import ABC, abstractmethod


class Character(ABC):
    """
    An abstract class representing a generic character.

    Attributes:
    -----------
    first_name : str
        The first name of the character.
    is_alive : bool
        A boolean flag indicating whether the character is alive. Default is True.

    Methods:
    --------
    die():
        Changes the character's alive status to False.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Initializes the character with a first name and alive status.

        Parameters:
        -----------
        first_name : str
            The first name of the character.
        is_alive : bool, optional
            A boolean flag indicating whether the character is alive. Default is True.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """
        Abstract method to change the character's alive status to False.
        Must be implemented by subclasses.
        """
        pass


class Stark(Character):
    """
    A class representing a Stark character, inheriting from the Character class.

    Attributes:
    -----------
    first_name : str
        The first name of the Stark character.
    is_alive : bool
        A boolean flag indicating whether the Stark character is alive. Default is True.

    Methods:
    --------
    die():
        Changes the Stark character's alive status to False.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Initializes the Stark character with a first name and alive status.

        Parameters:
        -----------
        first_name : str
            The first name of the Stark character.
        is_alive : bool, optional
            A boolean flag indicating whether the Stark character is alive. Default is True.
        """
        super().__init__(first_name, is_alive)

    def die(self):
        """
        Changes the Stark character's alive status to False.
        """
        self.is_alive = False


# Example usage:
if __name__ == "__main__":
    ned = Stark("Ned")
    print(f"{ned.first_name} is alive: {ned.is_alive}")  # Output: Ned is alive: True

    ned.die()
    print(f"{ned.first_name} is alive: {ned.is_alive}")  # Output: Ned is alive: False

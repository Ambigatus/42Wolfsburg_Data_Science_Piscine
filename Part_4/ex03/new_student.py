import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """
    Generate a random string of 15 lowercase letters to be used as an ID.

    :return: A random string of 15 lowercase letters.
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    A dataclass representing a student with a name, surname, active status,
    automatically generated login, and a random ID.
    """
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        """
        Automatically create the login from the first letter of the name
        and the full surname after initialization.
        """
        self.login = self.name[0] + self.surname

# Note: __str__ and __repr__ are automatically handled by the dataclass
# and should not be overwritten in this case.

import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate a random ID string of 15 lowercase letters.

    Returns:
        A random string of 15 lowercase letters.
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """A dataclass representing a student with auto-generated login and ID.

    Attributes:
        name: The student's first name.
        surname: The student's last name.
        active: Whether the student is active (default: True).
        login: Auto-generated login (first letter of name + surname in lowercase).
        id: Auto-generated random ID of 15 lowercase letters.
    """
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self) -> None:
        """Initialize the login field after instance creation.

        Creates login from first letter of name (uppercase) and surname (lowercase).
        """
        self.login = f"{self.name[0].upper()}{self.surname.lower()}"

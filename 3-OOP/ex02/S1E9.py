from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract base class representing a character with basic attributes and behaviors.

    This class serves as a template for creating character objects with a name and living status.
    Subclasses must implement the abstract methods.
    """

    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a character with a first name and living status.

        Args:
            first_name (str): The first name of the character
            is_alive (bool): Whether the character is alive (default: True)
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Mark the character as dead by setting is_alive to False."""
        self.is_alive = False


class Stark(Character):
    """Concrete implementation of Character representing a member of House Stark.

    This class inherits from Character and provides concrete implementations
    of all abstract methods.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a Stark character with a first name and living status.

        Args:
            first_name (str): The first name of the Stark character
            is_alive (bool): Whether the character is alive (default: True)
        """
        super().__init__(first_name, is_alive)

    def die(self):
        """Mark the Stark character as dead by calling the parent die method."""
        super().die()

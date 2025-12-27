from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Multiple inheritance class representing a King from both Baratheon and Lannister houses.

    This class demonstrates the diamond problem in multiple inheritance,
    where King inherits from both Baratheon and Lannister, which themselves
    inherit from Character. The class adds a title attribute and getter/setter methods
    for physical attributes.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a King character with attributes from both parent houses.

        Args:
            first_name (str): The first name of the King
            is_alive (bool): Whether the character is alive (default: True)
        """
        Lannister.__init__(self, first_name, is_alive)
        Baratheon.__init__(self, first_name, is_alive)

    def __str__(self):
        """String representation of the object"""
        return f'{self.first_name} {self.family_name} the {self.title} with {self.hairs} hair and {self.eyes} eyes.'

    def __repr__(self):
        """Developer-friendly representation of the object"""
        return f"{self.family_name}(first_name='{self.first_name}', is_alive={self.is_alive}), with {self.eyes} eyes and {self.hairs} hairs."

    def die(self):
        """Mark the King as dead by calling the parent die method."""
        super().die()

    def set_eyes(self, eye_color: str):
        """Set the eye color of the King.

        Args:
            eye_color (str): The new eye color
        """
        self.eyes = eye_color

    def get_eyes(self) -> str:
        """Get the eye color of the King.

        Returns:
            str: The eye color of the King
        """
        return self.eyes

    def set_hairs(self, hair_color: str):
        """Set the hair color of the King.

        Args:
            hair_color (str): The new hair color
        """
        self.hairs = hair_color

    def get_hairs(self) -> str:
        """Get the hair color of the King.

        Returns:
            str: The hair color of the King
        """
        return self.hairs

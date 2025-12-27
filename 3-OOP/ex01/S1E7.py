from S1E9 import Character


class Baratheon(Character):
    """Concrete implementation of Character representing a member of House Baratheon.

    Baratheon characters have brown eyes and dark hair by default.
    This class inherits from Character and adds family-specific attributes.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a Baratheon character with family-specific attributes.

        Args:
            first_name (str): The first name of the Baratheon character
            is_alive (bool): Whether the character is alive (default: True)
        """
        super().__init__(first_name, is_alive)
        self.family_name: str = "Baratheon"
        self.eyes: str = "brown"
        self.hairs: str = "dark"

    def __str__(self):
        """String representation of the object"""
        return f'{self.first_name} {self.family_name} with {self.hairs} hair and {self.eyes} eyes.'

    def __repr__(self):
        """Developer-friendly representation of the object"""
        return f"{self.family_name}(first_name='{self.first_name}', is_alive={self.is_alive}), with {self.eyes} eyes and {self.hairs} hairs."

    def die(self):
        """Mark the Baratheon character as dead by calling the parent die method."""
        super().die()


class Lannister(Character):
    """Concrete implementation of Character representing a member of House Lannister.

    Lannister characters have blue eyes and light hair by default.
    This class inherits from Character and adds family-specific attributes.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a Lannister character with family-specific attributes.

        Args:
            first_name (str): The first name of the Lannister character
            is_alive (bool): Whether the character is alive (default: True)
        """
        super().__init__(first_name, is_alive)
        self.family_name: str = "Lannister"
        self.eyes: str = "blue"
        self.hairs: str = "light"

    def __str__(self):
        """String representation of the object"""
        return f'{self.first_name} {self.family_name} with {self.hairs} hair and {self.eyes} eyes.'

    def __repr__(self):
        """Developer-friendly representation of the object"""
        return f"{self.family_name}(first_name='{self.first_name}', is_alive={self.is_alive}), with {self.eyes} eyes and {self.hairs} hairs."

    def die(self):
        """Mark the Lannister character as dead by calling the parent die method."""
        super().die()

    @staticmethod
    def create_lannister(first_name: str, is_alive: bool = True):
        """Factory method to create a Lannister instance.

        Args:
            first_name (str): The first name of the Lannister character
            is_alive (bool): Whether the character is alive (default: True)

        Returns:
            Lannister: A new Lannister instance
        """
        return Lannister(first_name, is_alive)

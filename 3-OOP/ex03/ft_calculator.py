class calculator:
    """A simple calculator class that performs basic arithmetic operations on a list of numbers."""

    def __init__(self, values: list[float]):
        """Initializes the calculator with a list of float values."""
        self.values = values

    def __add__(self, object) -> None:
        """Adds a number to each element in the values list."""
        self.values = [x + object for x in self.values]
        print(self.values)

    def __mul__(self, object) -> None:
        """Multiplies each element in the values list by a number."""
        self.values = [x * object for x in self.values]
        print(self.values)

    def __sub__(self, object) -> None:
        """Subtracts a number from each element in the values list."""
        self.values = [x - object for x in self.values]
        print(self.values)

    def __truediv__(self, object) -> None:
        """Divides each element in the values list by a number."""
        if object == 0:
            print("Error: Division by zero is not allowed.")
            return
        self.values = [x / object for x in self.values]
        print(self.values)

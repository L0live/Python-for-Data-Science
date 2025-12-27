class calculator:
    """A simple calculator class that performs basic arithmetic operations on a list of numbers."""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculates and prints the dot product of two vectors."""
        dot_product = sum(a * b for a, b in zip(V1, V2))
        print(f"Dot product: {dot_product}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Adds two vectors element-wise and prints the result."""
        added_vector = [float(a + b) for a, b in zip(V1, V2)]
        print(f"Added vector: {added_vector}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Subtracts the second vector from the first vector element-wise and prints the result."""
        subtracted_vector = [float(a - b) for a, b in zip(V1, V2)]
        print(f"Subtracted vector: {subtracted_vector}")

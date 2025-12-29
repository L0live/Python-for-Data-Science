def square(x: int | float) -> int | float:
    """Return the square of x.

    Args:
        x: A numeric value (int or float).

    Returns:
        The square of x.
    """
    return x * x


def pow(x: int | float) -> int | float:
    """Return x raised to the power of x.

    Args:
        x: A numeric value (int or float).

    Returns:
        x raised to the power of x.
    """
    return x ** x


def outer(x: int | float, function) -> object:
    """Create a closure that applies a function to x repeatedly.

    Args:
        x: Initial numeric value.
        function: A function to apply to x.

    Returns:
        A closure function that applies function to x and increments a counter.
    """
    count = 0

    def inner() -> float:
        """Apply the function to x and increment the counter.

        Returns:
            The result of applying function to x.
        """
        nonlocal count
        count += 1

        nonlocal x
        x = function(x)
        return x

    return inner

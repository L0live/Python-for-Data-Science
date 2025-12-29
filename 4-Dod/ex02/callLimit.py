def callLimit(limit: int):
    """Decorator factory to limit the number of times a function can be called.

    Args:
        limit: Maximum number of times the decorated function can be called.

    Returns:
        A decorator that limits function calls.
    """
    count = 0

    def callLimiter(function):
        """Decorator that wraps a function to limit its calls.

        Args:
            function: The function to wrap.

        Returns:
            The wrapped function with call limit.
        """
        def limit_function(*args: any, **kwds: any):
            """Wrapped function with call limit enforcement.

            Args:
                *args: Positional arguments to pass to the function.
                **kwds: Keyword arguments to pass to the function.

            Returns:
                The result of the function call if limit not reached, None otherwise.
            """
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Error: <function {function.__name__} at {hex(id(function))}> call too many times")
        return limit_function
    return callLimiter

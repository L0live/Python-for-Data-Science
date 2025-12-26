def all_thing_is_obj(object: any) -> int:
    """Display the type of an object.

    Args:
        object: Any Python object to inspect.

    Returns:
        int: Always returns 42.
    """
    print(object, ':', type(object))
    return 42

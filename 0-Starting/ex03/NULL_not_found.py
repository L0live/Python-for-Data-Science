def NULL_not_found(object: any) -> int:
    """Check if an object is a NULL-like value (None, NaN, empty, etc.).

    Args:
        object: Any Python object to check.

    Returns:
        int: 0 if NULL-like value found, 1 otherwise.
    """
    if object is None:
        print(f"Nothing: {object} {type(object)}")
    elif isinstance(object, bool) and object is False:
        print(f"Fake: {object} {type(object)}")
    elif isinstance(object, float) and str(object) == 'nan':
        print(f"Cheese: {object} {type(object)}")
    elif isinstance(object, int) and object == 0:
        print(f"Zero: {object} {type(object)}")
    elif isinstance(object, str) and object == "":
        print(f"Empty: {object} {type(object)}")
    else:
        print("Type not found")
        return 1
    return 0

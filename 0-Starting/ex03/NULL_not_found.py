def NULL_not_found(object: any) -> int:
    """Check if an object is a NULL-like value (None, NaN, empty, etc.).
    
    Args:
        object: Any Python object to check.
    
    Returns:
        int: 0 if NULL-like value found, 1 otherwise.
    """
    if not object or object != object:
        print(object, ':', type(object))
        return 0
    return 1
def NULL_not_found(object: any) -> int:
    if not object or object != object:
        print(object, ':', type(object))
        return 0
    return 1

def ft_filter(func, list):
    """Filter a list using a predicate function.
    
    Args:
        func: Function that returns True/False for each element.
        list: List to filter.
    
    Returns:
        list: Filtered list containing only elements where func(x) is True.
    """
    return [x for x in list if func(x)]

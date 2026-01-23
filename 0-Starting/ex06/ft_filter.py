
def ft_filter(func, list):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""

    if func is None:
        return [x for x in list if x]
    return [x for x in list if func(x)]

def ft_mean(values: list[float]) -> float:
    """Calculate the mean of a list of float values."""
    return sum(values) / len(values) if values else 0.0


def ft_median(values: list[float]) -> float:
    """Calculate the median of a list of float values."""
    sorted_values = sorted(values)
    n = len(sorted_values)
    if n == 0:
        return 0.0
    mid = n // 2
    if n % 2 == 0:
        return (sorted_values[mid - 1] + sorted_values[mid]) / 2
    else:
        return sorted_values[mid]


def ft_quartile(values: list[float]) -> list[float]:
    """Calculate the first and second quartiles of a list of float values.
    1, 42, 360, 11, 64 -> Q1=11, Q3=64
    """
    sorted_values = sorted(values)
    n = len(sorted_values)
    if n == 0:
        return [0.0, 0.0]
    mid = n // 2

    q1 = float(sorted_values[:mid][1])
    q3 = float(sorted_values[mid + (1 if n % 2 else 0):][0])
    return [q1, q3]


def ft_std(values: list[float]) -> float:
    """Calculate the standard deviation of a list of float values."""
    n = len(values)
    if n == 0:
        return 0.0
    mean = ft_mean(values)
    variance = sum((x - mean) ** 2 for x in values) / n
    return variance ** 0.5


def ft_var(values: list[float]) -> float:
    """Calculate the variance of a list of float values."""
    n = len(values)
    if n == 0:
        return 0.0
    mean = ft_mean(values)
    return sum((x - mean) ** 2 for x in values) / n


def ft_statistics(*args: any, **kwargs: any) -> None:
    """Calculate and print statistical measures based on provided numerical arguments and measures as arguments.

    Args:
        *args: Variable length argument list of numerical values.
        **kwargs: Keyword arguments where values are statistical measures to compute.
    """
    for _, measure in kwargs.items():
        if not args:
            print(f"No data provided for calculating {measure}.")
            continue
        if not all(isinstance(v, (int, float)) for v in args):
            print(f"Non-numeric data provided for calculating {measure}.")
            continue
        result = None
        if measure == "mean":
            result = ft_mean(args)
        elif measure == "median":
            result = ft_median(args)
        elif measure == "quartile":
            result = ft_quartile(args)
        elif measure == "std":
            result = ft_std(args)
        elif measure == "var":
            result = ft_var(args)

        if result is not None:
            print(f"{measure} : {result}")

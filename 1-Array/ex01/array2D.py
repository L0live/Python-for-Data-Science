import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Slice a 2D array and display its shape before and after slicing.
    
    Args:
        family: 2D list to slice.
        start: Starting index for the slice.
        end: Ending index for the slice.
    
    Returns:
        list: Sliced 2D list.
    """
    assert len(family) > 0, "Input list must have a positive length."
    assert isinstance(family, list) and all(isinstance(sublist, list) for sublist in family), "Input must be a 2D list."
    assert all(len(sublist) == len(family[0]) for sublist in family), "All sublists must have the same length."
    assert isinstance(start, int) and isinstance(end, int), "Start and end indices must be integers."

    family_array = np.array(family)
    print("My shape is :", family_array.shape)
    sliced_array = family_array[start:end]
    print("My new shape is :", sliced_array.shape)

    return sliced_array.tolist()

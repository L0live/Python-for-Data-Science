import numpy as np


def ft_invert(array) -> np.array:
    invert_array = np.array([[[255 - array[i, j, 0], 255 - array[i, j, 1], 255 - array[i, j, 2]] for j in range(array.shape[1])] for i in range(array.shape[0])])
    return invert_array

def ft_red(array) -> np.array:
    red_array = np.array([[[array[i, j, 0], 0, 0] for j in range(array.shape[1])] for i in range(array.shape[0])])
    return red_array

def ft_green(array) -> np.array:
    green_array = np.array([[[0, array[i, j, 1], 0] for j in range(array.shape[1])] for i in range(array.shape[0])])
    return green_array

def ft_blue(array) -> np.array:
    blue_array = np.array([[[0, 0, array[i, j, 2]] for j in range(array.shape[1])] for i in range(array.shape[0])])
    return blue_array

def ft_grey(array) -> np.array:
    # grey_array = np.array([[[int(array[i, j, 0] / 3), int(array[i, j, 1] / 3), int(array[i, j, 2] / 3)] for j in range(array.shape[1])] for i in range(array.shape[0])])
    return array[:, :, 1]

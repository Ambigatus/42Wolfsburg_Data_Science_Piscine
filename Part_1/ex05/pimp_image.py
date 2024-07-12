import numpy as np


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Inverts the colors of the image.

    Parameters:
    array (np.ndarray): The input image array.

    Returns:
    np.ndarray: The color-inverted image array.
    """
    inverted_array = 255 - array
    return inverted_array


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Retains only the red channel.

    Parameters:
    array (np.ndarray): The input image array.

    Returns:
    np.ndarray: The image array with only the red channel.
    """
    red_array = array.copy()
    red_array[:, :, 1] = 0  # Set green channel to 0
    red_array[:, :, 2] = 0  # Set blue channel to 0
    return red_array


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Retains only the green channel.

    Parameters:
    array (np.ndarray): The input image array.

    Returns:
    np.ndarray: The image array with only the green channel.
    """
    green_array = array.copy()
    green_array[:, :, 0] = 0  # Set red channel to 0
    green_array[:, :, 2] = 0  # Set blue channel to 0
    return green_array


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Retains only the blue channel.

    Parameters:
    array (np.ndarray): The input image array.

    Returns:
    np.ndarray: The image array with only the blue channel.
    """
    blue_array = array.copy()
    blue_array[:, :, 0] = 0  # Set red channel to 0
    blue_array[:, :, 1] = 0  # Set green channel to 0
    return blue_array


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Converts the image to grayscale.

    Parameters:
    array (np.ndarray): The input image array.

    Returns:
    np.ndarray: The grayscale image array.
    """
    grey_array = np.mean(array, axis=2, dtype=int)
    return grey_array

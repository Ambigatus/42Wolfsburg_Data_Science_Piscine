import numpy as np
from PIL import Image


def ft_load(image_path: str) -> np.ndarray:
    """
    Loads an image from the specified path and returns it as a numpy array.

    Parameters:
    image_path (str): The path to the image file.

    Returns:
    np.ndarray: The image as a numpy array.
    """
    image = Image.open(image_path)
    image_array = np.array(image)
    return image_array

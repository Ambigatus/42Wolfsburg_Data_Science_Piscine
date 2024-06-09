from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
        Load an image, print its format and return its pixel content in RGB format.

        Args:
            path (str): The path to the image file.

        Returns:
            np.ndarray: The pixel content of the image in RGB format.

        Raises:
            ValueError: If the image format is not supported.
            FileNotFoundError: If the image file does not exist.
            Exception: For any other errors.
        """
    try:
        with Image.open(path) as img:
            if img.format not in ["JPEG", "PNG", "BMP", "JPG"]:
                raise ValueError("Unsupported image format. Supported formats are JPEG, PNG, BMP, JPG.")

            img_rgb = img.convert("RGB")

            pixels = np.array(img_rgb)

            print(f"The shape of the image is: {pixels.shape}")
            return pixels
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {path} does not exist.")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")

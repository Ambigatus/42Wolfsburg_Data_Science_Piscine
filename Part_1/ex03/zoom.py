import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def ft_zoom(image_array: np.ndarray, zoom_factor: float):
    """
    Zoom into the image by the specified zoom factor.

    Args:
        image_array (np.ndarray): Pixel content of the image.
        zoom_factor (float): Factor by which to zoom the image.

    Returns:
        np.ndarray: Zoomed version of the image.
    """
    try:
        if zoom_factor <= 0:
            raise ValueError("Zoom factor must be greater than 0.")

        height, width, channels = image_array.shape
        new_height, new_width = int(height * zoom_factor), int(width * zoom_factor)

        # Checks dimensions are within the original image
        new_height = min(new_height, height)
        new_width = min(new_width, width)

        # Perform slicing for zoom
        start_y = (height - new_height) // 2
        start_x = (width - new_width) // 2
        zoomed_image = image_array[start_y:start_y + new_height, start_x:start_x + new_width]

        # Print the new shape
        print(f"New shape after slicing: {zoomed_image.shape}")
        print(zoomed_image)

        return zoomed_image
    except Exception as e:
        print(f"An error occurred: {e}")


def display_image_with_scale(image_array: np.ndarray, title: str):
    """
    Display the image with the scale.

    Args:
        image_array (np.ndarray): Pixel content of the image.
        title (str): Title of the image.
    """
    try:
        plt.imshow(image_array)
        plt.title(title)
        plt.xlabel("Width")
        plt.ylabel("Height")
        plt.show()
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    """
    Main function to demonstrate the zoom functionality.
    """
    image_path = "animal.jpeg"

    # Load the image
    image_array = ft_load(image_path)

    if image_array is not None:
        zoomed_image = ft_zoom(image_array, 0.5)

        if zoomed_image is not None:
            display_image_with_scale(zoomed_image, "Zoomed Image")


if __name__ == "__main__":
    main()
# The zoom function takes the pixel content of an image and a zoom factor as input. It then calculates the new
# dimensions of the zoomed image and performs slicing to zoom into the center of the image.
# The display_image_with_scale function is used to display the zoomed image with the scale.
# The main function loads an image, zooms into it, and displays the zoomed image.

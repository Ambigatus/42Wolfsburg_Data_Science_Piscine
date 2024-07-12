from PIL import Image


def load_image(image_path):
    """
    Load an image and convert it to grayscale.

    Parameters:
    - image_path (str): Path to the image file.

    Returns:
    - Image: Grayscale image.
    """
    image = Image.open(image_path).convert('L')  # Convert to grayscale
    return image


def cut_square(image, size=400):
    """
    Cut a square region from the center of the image.

    Parameters:
    - image (Image): Grayscale image.
    - size (int): Size of the square to cut from the center.

    Returns:
    - Image: Cropped square image.
    """
    width, height = image.size
    left = (width - size) // 2
    top = (height - size) // 2
    right = left + size
    bottom = top + size
    square_image = image.crop((left, top, right, bottom))
    return square_image

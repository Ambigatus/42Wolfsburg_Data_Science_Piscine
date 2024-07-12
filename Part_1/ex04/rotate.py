import numpy as np
from PIL import Image
from load_image import load_image, cut_square


def transpose_image(image):
    """
    Transpose the image array.

    Parameters:
    - image (Image): Grayscale image.

    Returns:
    - tuple: Transposed numpy array and the corresponding image.
    """
    image_array = np.array(image)
    transposed_array = image_array.T  # Transpose the array
    transposed_image = Image.fromarray(transposed_array)
    return transposed_array, transposed_image


if __name__ == "__main__":
    image_path = 'animal.jpeg'  # Path to your image

    # Load and preprocess the image
    image = load_image(image_path)
    square_image = cut_square(image)

    # Transpose the square image
    transposed_array, transposed_image = transpose_image(square_image)

    # Display the transposed image
    transposed_image.show()

    # Print the original and transposed shapes and data
    print(f"The shape of image is: {square_image.size}")
    print(np.array(square_image))
    print(f"New shape after Transpose: {transposed_array.shape}")
    print(transposed_array)

"""
1. Loading the Image: We start by loading the image from a file.

2. Converting to Grayscale: We convert the image to grayscale. This simplifies the image to a 2D array because grayscale
images have only one channel (intensity) as opposed to three channels (RGB) in colored images.

3. Cropping the Image: We crop a square part of the grayscale image to ensure that the array is square, as the task
requires.

4. Transposing the Array: We transpose the 2D array of the cropped grayscale image. Transposing swaps the rows and
columns of the array.

5. Displaying and Printing the Result: Finally, we display the transposed image, and print the new shape and data 
of the transposed image.
"""

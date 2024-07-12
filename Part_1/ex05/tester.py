# tester.py

from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
import matplotlib.pyplot as plt

# Load the image
image_path = "landscape.jpg"
array = ft_load(image_path)

# Apply filters
inverted_image = ft_invert(array)
red_image = ft_red(array)
green_image = ft_green(array)
blue_image = ft_blue(array)
grey_image = ft_grey(array)

# Print documentation and results
print(ft_invert.__doc__)
print("Inverted Image:")
print(inverted_image)

print(ft_red.__doc__)
print("Red Filtered Image:")
print(red_image)

print(ft_green.__doc__)
print("Green Filtered Image:")
print(green_image)

print(ft_blue.__doc__)
print("Blue Filtered Image:")
print(blue_image)

print(ft_grey.__doc__)
print("Greyscale Image:")
print(grey_image)


# Function to display an image
def display_image(image, title):
    plt.imshow(image, cmap='gray' if len(image.shape) == 2 else None)
    plt.title(title)
    plt.axis('off')


# Display the images
plt.figure(figsize=(10, 10))

plt.subplot(231)
display_image(array, 'Original Image')

plt.subplot(232)
display_image(inverted_image, 'Inverted Image')

plt.subplot(233)
display_image(red_image, 'Red Filtered Image')

plt.subplot(234)
display_image(green_image, 'Green Filtered Image')

plt.subplot(235)
display_image(blue_image, 'Blue Filtered Image')

plt.subplot(236)
display_image(grey_image, 'Greyscale Image')

plt.tight_layout()
plt.show()

# Importing the necessary libraries
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# Defining a function to rotate an image recursively
def rotationImage(image):
    """
    Effectue une rotation de l'image donnée.

    Args:
        image (numpy.ndarray): L'image à faire pivoter.

    Returns:
        numpy.ndarray: L'image pivotée.
    """
    n = len(image)
    if n > 1:
        # Splitting the image into four quadrants and rotating them recursively
        temp = np.copy(image[n//2:, :n//2])
        image[n//2:, :n//2] = rotationImage(image[n//2:, n//2:])
        image[n//2:, n//2:] = rotationImage(image[:n//2, n//2:])
        image[:n//2, n//2:] = rotationImage(image[:n//2, :n//2])
        image[:n//2, :n//2] = rotationImage(temp)
    return image

# Loading an image and displaying it
imag = np.array(Image.open('chien256_256.jpg'))
img = plt.imshow(imag)
plt.show()

# Rotating the image and displaying the rotated image
imageRot = rotationImage(imag)
imR = plt.imshow(imageRot)
plt.show()

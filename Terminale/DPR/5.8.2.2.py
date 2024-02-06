# Importation des bibliothèques nécessaires
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# Chargement de l'image en tant que tableau numpy
imag = np.array(Image.open('chien256_256.jpg'))

# Rotation de l'image à l'aide de la fonction np.rot90()
imagRot = Image.fromarray(np.rot90(imag))

# Sauvegarde de l'image rotée
imagRot.save("rotationTableauChien256_256.jpg")

# Affichage de l'image rotée
imagRot.show()

# Affichage de l'image originale à l'aide de matplotlib
imag1 = plt.imshow(imag)
plt.show()

# Affichage de l'image rotée à l'aide de matplotlib
imag2 = plt.imshow(imagRot)
plt.show()
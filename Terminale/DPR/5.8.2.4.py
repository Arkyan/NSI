# Importation des bibliothèques nécessaires
from PIL import Image  # Pour manipuler les images
import matplotlib.pyplot as plt  # Pour afficher les images
import numpy as np  # Pour manipuler les tableaux

# Définition de la fonction de rotation d'image
def rotationImage(img):
    # Création d'une liste vide pour stocker l'image tournée
    imageTournee = [[] for x in range(len(img))]
    
    # Parcours de l'image d'origine
    for i in range(len(img)):
        for j in range(len(img[i])):
            # Rotation de chaque pixel et ajout dans la liste de l'image tournée
            imageTournee[i].append(img[len(img) - 1 - j][i])
    
    # Retourne l'image tournée
    return imageTournee

# Chargement de l'image et conversion en tableau numpy
imag = np.array(Image.open('chien256_256.jpg'))

# Affichage de l'image d'origine
img = plt.imshow(imag)
plt.show()

# Rotation de l'image
imageRot = rotationImage(imag)

# Affichage de l'image tournée
imR = plt.imshow(imageRot)
plt.show()

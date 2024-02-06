from PIL import Image

# Ouvrir l'image
image = Image.open("chien256_256.jpg")

# Obtenir les dimensions de l'image
largeur, hauteur = image.size
print("Dimensions de l'image : largeur", largeur, "pixels, hauteur", hauteur, "pixels")

# Afficher l'image
image.show()

# Calculer les nouvelles dimensions de l'image
nouvelleLargeur = int(largeur / 1.1)
nouvelleHauteur = hauteur * 2

# Redimensionner l'image
image_redimensionnee = image.resize((nouvelleLargeur, nouvelleHauteur))

# Obtenir les dimensions de l'image redimensionnée
largeur_redimensionnee, hauteur_redimensionnee = image_redimensionnee.size
print("Dimensions de l'image modifiée : largeur", largeur_redimensionnee, "pixels, hauteur", hauteur_redimensionnee, "pixels")

# Enregistrer l'image redimensionnée
image_redimensionnee.save("nouveauChien256_256.jpg")

# Afficher l'image redimensionnée
image_redimensionnee.show()

# Obtenir les coordonnées du pixel
coordonneesPixel = (0, 0)
pixelRVB = image.getpixel(coordonneesPixel)
print("Le pixel de coordonnées", coordonneesPixel, "a pour code RVB/RGB", pixelRVB)

# Ouvrir une nouvelle instance de l'image originale
image_inverse = Image.open("chien256_256.jpg")

# Inverser les couleurs de l'image
for abscisse in range(int(largeur / 4), int(largeur / 4) + int(largeur / 2)):
    for ordonnee in range(int(hauteur / 4), int(hauteur / 4) + int(hauteur / 2)):
        R, V, B = image_inverse.getpixel((abscisse, ordonnee))
        nouveauR, nouveauV, nouveauB = 255 - R, 255 - V, 255 - B
        image_inverse.putpixel((abscisse, ordonnee), (nouveauR, nouveauV, nouveauB))

# Afficher l'image inversée
image_inverse.show()

# Enregistrer l'image inversée
image_inverse.save("inverseChien256_256.jpg")

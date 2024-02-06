from PIL import Image

# Ouvrir l'image
imag = Image.open("chien256_256.jpg")

# Effectuer une rotation de -45 degrés
imagRot1 = imag.rotate(angle=-45)

# Effectuer une rotation de 45 degrés avec agrandissement
imagRot2 = imag.rotate(angle=45, expand=1)

# Effectuer une rotation de -70 degrés avec agrandissement et remplissage de couleur jaune
imagRot3 = imag.rotate(angle=-70, expand=1, fillcolor='yellow')

# Effectuer une rotation de -80 degrés avec agrandissement et remplissage de couleur blanche
imagRot4 = imag.rotate(angle=-80, expand=1, fillcolor='white')

# Effectuer une rotation de -90 degrés
imagRot5 = imag.rotate(angle=-90)

# Enregistrer les images résultantes
imagRot5.save("rotation-90Chien256_256.jpg")
imagRot4.save("rotation-80Chien256_256.jpg")
imagRot3.save("rotation-70Chien256_256.jpg")
imagRot2.save("rotation45Chien256_256.jpg")
imagRot1.save("rotation-45Chien256_256.jpg")

# Afficher les images résultantes
imagRot1.show()
imagRot2.show()
imagRot3.show()
imagRot4.show()
imagRot5.show()

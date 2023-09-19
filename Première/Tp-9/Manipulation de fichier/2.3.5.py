#Fichiers, lecture ligne à ligne
#Importation des bibliothèques
import os
#Ouvrir le fichier dataLettre.txt en lecture
fichierTexte = open("dataNombre.txt" , "r")

#Afficher le contenu du fichier contenu du ficher dataNombre.txt
contenu = fichierTexte.read()
print(contenu)

#Fermer le fichier dataNombre.txt
fichierTexte.close()
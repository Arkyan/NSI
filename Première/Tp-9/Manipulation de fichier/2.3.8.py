#Fichiers, lecture et stockage dans une liste
#Importation des bibliothèques
import os

#Ouvir le fichier dataNombre.txt en lecture
fichierTexte = open("dataNombre.txt" , "r")

#Afficher le contenu du fichier dataNombre.txt dans une liste
contenuFichier = fichierTexte.readlines()
print("Le fichier contient :", contenuFichier)

#Fermer le fichier dataNombre.txt
fichierTexte.close
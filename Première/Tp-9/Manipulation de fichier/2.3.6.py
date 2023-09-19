#Fichiers, lecture ligne à ligne
#Importation des bibliothèques 
import os

#Ouvrir le fichier dataLettres.txt en lecture 
fichierTexte = open("dataLettres.txt", "r")

#Afficher le contenu du fichier dataLettres.txt ligne à ligne
numero = 1
for ligne in fichierTexte:
    print("Ligne n°", numero, "contient :", ligne)
    numero = numero + 1

#Fermer le fichier dataLettre.txt
fichierTexte.close() 
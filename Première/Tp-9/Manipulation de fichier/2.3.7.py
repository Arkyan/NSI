#Fichiers, lecture ligne à ligne avec in range
#Importation des bibliothèques
import os
#Ouvrir le fichier dataLettres.txt en lecture
fichierTexte = open("dataLettres.txt", "r")

#Afficher le contenu du fichier dataLettres.txt ligne à ligne
for numero in range (1,9) :
    contenuLigne = fichierTexte.readline()
    print("Ligne n°", numero, "contient :", contenuLigne)

#Fermer le fichier dataLettre.txt
fichierTexte.close()
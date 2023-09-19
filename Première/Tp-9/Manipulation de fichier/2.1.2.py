#Ouvrir le fichier data.txt en écriture
fichierTexte = open("data.txt", "w")

#Ecrire Bonjour à la ligne (\n) dans le fichier data.txt
fichierTexte.write("\nBonjour")

#Ecrire 1234 à la ligne suivante (\n) dans la fichier data.txt
fichierTexte.write("\n1234")

fichierTexte.close()
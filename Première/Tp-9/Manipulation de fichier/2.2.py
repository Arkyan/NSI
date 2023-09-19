#Fichiers
#Importation des bibliothèques
import os

#Fournir le répertoire courant de travail
chemin = os.getcwd()

#Afficher le répertoire courant de travail
print(chemin)

#Change de répertoire courant de travail, chemin absolu
#os.chdir("d:\\NSI\\Tp-9")

#Afficher le répertoire courant de travail
print(os.getcwd())

#Affciher les fichiers contenus dans le répertoire de travail
listfichier = os.listdir()

print(listfichier)

#Change de répertoire courant de travail, remonte de 1 niveau dans l'arborescence, chemin relatif 
os.chdir(". .")

#Fournir le répertoire courant de travail
chemin = os.getcwd

#Afficher le répertoire courant de travail
print(os.getcwd())

#Ouvrir le fichier data.txt en écriture
fichierTexte = open("data.txt", "w")

#Ouvrir le fichier data.txt en écriture
fichierTexte = open("data.txt", "w")

#Ecrire Bonjour à la ligne (\n) dans le fichier data.txt
fichierTexte.write("\nBonjour")

#Ecrire 1234 à la ligne suivante (\n) dans la fichier data.txt
fichierTexte.write("\n1234")

fichierTexte.close()
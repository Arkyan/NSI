#Importation du module pour les fichiers csv
import csv

#Ouverture du ficher en lecture
fichier = open("testcsv.csv" , "r")

#Initialisation d'un lecteur de fichier delimiter est facultatif
csv_en_liste = csv.reader(fichier , delimiter = "," )

#parcours du lecteur avec pour
for ligne in csv_en_liste :
    #Affichage ligne à ligne
    print(ligne)
    #Affichage du type de chaque ligne
    print(type(ligne))

#Fermeture du fichier
fichier.close()
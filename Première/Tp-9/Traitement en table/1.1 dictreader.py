#Importation du module pour les fichiers csv
import csv

#Ouverture du fichier csv en lecture
fichier = open("testcsv.csv" , "r")

#Initialisation d'un lecteur de fichier avec crétaion d'un dico, delimiter est facultatif
csv_en_dico = csv.DictReader(fichier , delimiter = ",")

#Parcours du lecteur avec une boucle pour
for ligne in csv_en_dico :
    #Affichage ligne à ligne de la liste de tuples
    print(ligne)
    #Affichage ligne à ligne du dico
    print(dict(ligne))
    #Afffichage de la valeur correspondant à la clé prénom
    print(dict(ligne)["PRÉNOM"])
    #Afficghae du type de chaque ligne
    print(type(ligne))

#Fermeture du fichier
fichier.close()
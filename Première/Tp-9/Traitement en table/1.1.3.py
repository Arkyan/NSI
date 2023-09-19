#Importation du module pour les fichiers csv
import csv

#Fonction qui renvoie une liste de dictionnaire obtenue avec la fonction dictreader
def importe(nom) : 
    #ouverture du fichier csv en lecture 
    with open(nom + ".csv", "r") as fichier :
        #Initialistaion d'un lecteur de fichier avec création d'un dico
        csvendico = csv.DictReader(fichier, delimiter = ",")
        #Création de la liste de dictionnaire correspondant au fichier csv avec pârcours à l'aide d'une boucle pour
        listdico = [dict(ligne) for ligne in csvendico]

    #Fermer le fichier csv au retour de l'indentation
    #Retourner la liste de dictionnaire
    return listdico

#Afficher la liste de dictionnaire
print(importe("testcsv"))

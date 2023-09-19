#Importation du module pour les fichiers csv
import csv

#Fonction qui renvoie une liste de dictionnaire obtenue avec la fonction dictreader
def importe(nom) :
    #ouverture du fichier csv en lecture
    fichier = open(nom +".csv","r")
    #Initialisation d'un lecteur de fichier avec création dd'un dico
    csv_en_dico = csv.DictReader(fichier, delimiter=",")
    #Création de la liste de dictionnaire correspondant au fichier csv avec parcours à l'aide d'une boucle pour
    list_dico = [dict(ligne) for ligne in csv_en_dico]
    #Fermer le fichier csv
    fichier.close()
    #Retourner la liste de dico
    return list_dico

#Afficher la liste de dico
print(importe("testcsv"))
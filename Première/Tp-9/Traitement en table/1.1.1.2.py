#Importation du module pour les fichiers csv
import csv

#Fonction qui renvoie une liste de la liste obtenue avec la fonction reader
def csv_en_list_de_list2(nom) :
    #Ouverture du fichier csv en lecture
    fichier = open(nom +".csv","r")
    #Création de la liste de liste correspondant au fichier csv avec parcours à l'aide d'une boucle pour
    list_de_list = [ligne for ligne in csv.reader(fichier,delimiter=",")]
    #Fermer le fichier csv
    fichier.close()
    #retourner la liste de liste
    return list_de_list

#Afficher la liste de liste 
print(csv_en_list_de_list2("testcsv"))
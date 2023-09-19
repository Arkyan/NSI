#Importation du module pour les fichiers csv
import csv

#Fonction qui renvoie une liste de la liste obtenue avec la fonction reader
def csv_en_list_de_list(nom) :
    #Création d'une lsitye vide
    list_de_list = []
    #Ouverture du fichier csv en lecture
    fichier = open(nom +".csv","r")
    #Création de la liste correspondant au fichier csv
    csv_en_list = csv.reader(fichier,delimiter = ",")
    #parcours de la liste avec une boucle pour
    for ligne in csv_en_list :
        #Affichage de la ligne
        print(ligne)
        #Ajouter une liste à une liste
        list_de_list.append(ligne)
    #Fermer le fichier csv
    fichier.close()
    #Retourner la liste de liste
    return list_de_list

#Afficher la liste de liste
print(csv_en_list_de_list("testcsv"))
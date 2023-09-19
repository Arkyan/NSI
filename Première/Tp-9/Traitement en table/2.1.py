#Importation du module pour les fichiers csv 
import csv

#Fonction qui renvoie une liste de dico obtenue avec la fonction DictReader()
def importe(nom) :
    #Ouverture du fichier csv en lecture 
    fichier = open(nom+".csv","r")
    #Initialisation d'un lecteur de fichier avec création d'un dico
    csvendico = csv.DictReader(fichier,delimiter=",")
    #Création de la liste de dico correspondant au fichier csv à l'aide d'une boucle pour
    list_dico = [dict(ligne) for ligne in csvendico]
    #Fermer le fichier csv
    fichier.close()
    #Retourner la list de dico 
    return list_dico

#Création d'une liste de dico à partir du fichier csv
liste_dico = importe("testcsv")
print(liste_dico)
#Création par compréhension d'une liste de dico ayant certains critères
liste_recherche = [p for p in liste_dico if p["NOM"] == ["Clanget"]]
print(liste_recherche)
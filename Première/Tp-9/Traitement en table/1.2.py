

#Importation du module pour les fichiers csv
import csv

#Fonction qui renvoie un fichier csv à partir d'une liste de dico
#Paramètre: NomDeLaTable = chaine de caractère indiquant le nom de la liste de dictionnaire
#           Ordre = correspond à l'ordre des clés du dictionnaire
#           NomDuFichierCsv = chaine de caractère indiquant le nom du fichier csv
def vers_csv (nomdelatable,ordre,nomdufichiercsv) :
    #Compléter table avec les données contenues dans la liste de dicos nommée NomDeLaTable
    table = eval("nomdelatable")

    #Ouverture du fichier csv en écriture et stockage dans la variable fichier 
    with open(nomdufichiercsv+'.csv',"w") as fichier :
        #Création du dictionnaire dict avec la fonction DictWriter() du module csv et avec les clés se trouvant dans ordre
        dict = csv.DictWriter(fichier,fieldnames=ordre)

        #Création de la première ligne comportant le nom des champs correspondants aux clés des dictionnaires
        dict.writeheader()
        
        #Pour chaque ligne de la table, insérer dans dict la ligne de table
        for ligne in table :
            dict.writerow(ligne)
    #fermer le fichier csv au retour de l'indentation
    return None

tableExemple = [{'nom': 'Dupont', 'prenom': 'Jean-Claude', 'age' :'32'} , {'nom': 'Duteil', 'prenom': 'Paul', 'age' :'41'} , {'nom': 'Claudon', 'prenom': 'Goery', 'age' :'37'} , {'nom': 'Tonton', 'prenom': 'Pierre54', 'age' :'None'} , {'nom': 'Penard', 'prenom': 'Bob', 'age' :'18'} , {'nom': 'Herpoix', 'prenom': 'Stephane', 'age' :':55'} , {'nom': 'Salicorne', 'prenom': 'Bruno', 'age' :'15'} , {'nom': 'Poiteau', 'prenom': 'Maxe', 'age' :'33'} , {'nom': 'Clanget', 'prenom': 'Gilles', 'age' :'54'} , {'nom': 'Luillier', 'prenom': 'Martin', 'age' :'34'} , {'nom': 'Clanget', 'prenom': 'Justine', 'age' :'14'} , {'nom': 'Gillier', 'prenom': 'Paul', 'age' :'16'}]
ordre = ["prenom","nom","age"]
nomdufichiercsv = "fichier_csv"
vers_csv(tableExemple,ordre,nomdufichiercsv)
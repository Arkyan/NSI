#Déclaration et remplissage d'un dictionnaire 
mondico = {"nom" : "Dupont" , "prenom" : "Paul" , "date de naissance" : "01/04/2020"}
#Où
mondico1 = {} #Déclarer un dictionnaire vide 
mondico1["nom"] = "Durand" #Ajouter un couple clé/valeur
mondico1["prenom"] = "Pierre" #Ajouter un couple clé/valeur
mondico1["date de naissance"] = "01/04/2020" #Ajouter un couple clé/valeur

#Afficher le dictionnaire
print("Le premier dictionnaire est :", mondico)
print("Le deuxième dictionnaire est :", mondico1)

#Afficher la valeur associé à la clé
print("Bonjour, je m'appelle",mondico["prenom"], mondico["nom"],",je suis née le ",mondico["date de naissance"], ", mon grand père se nomme", mondico1["prenom"],mondico1["nom"], "et il est né le ", mondico1["date de naissance"])

#Modifier la valeur d'une clé, les dictionnaires sont mutables 
mondico1["date de naissance"] = "02/04/1972"

#Ajouter un couple clé/valeur, les dictionnaires sont mutables 
mondico1["lieu de naissance"] = "Limoges" 
print("Bonjour, je m'appelle", mondico["prenom"], mondico["nom"], ", je suis né le ", mondico["date de naissance"],", mon grand père se nomme",mondico1["prenom"],mondico1["nom"],"et il est né le",mondico1["date de naissance"],"à",mondico1["lieu de naissance"])

#Supprimer un couple clé/valeur, les dictionnaires sont mutables
del mondico1["lieu de naissance"]
print("Le deuxième dictionnaire sans lieu de naisssance est :",mondico1)

#Modifier la valeur d'une clé par copie
mondico1["prenom"] = mondico["prenom"]
print("Bonjour, je m'appelle",mondico["prenom"],mondico["nom"],",")

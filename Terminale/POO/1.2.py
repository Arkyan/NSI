class ClasseVelo : #Définition de la classe 
                   #Documentation / Docstring
    """
    Classe ClasseVelo permettant de créer des
    instances de vélo ayant pour attributs :
    le nombre de roues : un entier
    la marque : un str
    le prix : un entier
    la masse : un entier 
    """
    roues = 2 #Variable de classe permettant de stocker
              #un attribut "roues" communs à toutes les
              #instances de la classe "ClasseVelo"

            #Méthode init appellée à la création de l'objet
    def __init__(self, marque, prix, masse) : #Définition du constructeur,variables d'instances uniques pour chaque instance
        self.marque = marque #1er attribut : la marque
        self.prix = prix #2e attribut : le prix
        self.masse = masse #3e : la masse

velo1 = ClasseVelo("btwin",250,25) #Instanciation / Création de l'objet "velo1"
velo2 = ClasseVelo("rockrider",170,12) #Instanciation / Création de l'objet "velo2"

print("L'objet velo1 ", velo1)
print("L'objet velo2 ", velo2)
print("Le nombre de roues de velo 1 est : ", velo1.roues)
print("Le nombre de roues de velo 2 est : ", velo2.roues)
print("La marque de velo1 est : ", velo1.marque)
print("La marque de velo2 est : ", velo2.marque)
print("Le prix develo1 est : ", velo1.prix)
print("La masse de velo2 est : ", velo2.masse)
class Arbre: # Arbre binaire en POO
    def __init__(self,valeur):
        self._racine = valeur
        self._gauche = None
        self._droite = None
    def set_gauche(self, sousarbre):
        self._gauche = sousarbre
    def set_droite(self, sousarbre):
        self._droite = sousarbre
    def get_gauche(self):
        return self._gauche
    def get_droite(self):
        return self._droite 
    def get_racine(self):
        return self._racine
    def __str__(self):
        return "({},{},{})".format(self._gauche, self._racine,self._droite)

arbr = Arbre(4)
print(arbr)
arbr.set_gauche(Arbre(3))
print(arbr)
arbr.set_droite(Arbre(1))
print(arbr)
arbr.get_droite().set_gauche(Arbre(2))
print(arbr)
arbr.get_droite().set_droite(Arbre(7))
print(arbr)
arbr.get_gauche().set_gauche(Arbre(6))
print(arbr)
arbr.get_droite().get_droite().set_gauche(Arbre(9))
print(arbr)

print("La racine du sag du sad de l'arbre est : ", arbr.get_droite().get_gauche().get_racine())
print("La racine du sag du sad de l'arbre est : ", arbr.get_gauche().get_gauche().get_racine()) 
print("La racine du sag du sad de l'arbre est : ", arbr.get_droite().get_droite().get_gauche().get_racine()) 

from queue import Queue

def BFS(arbre):
    file = Queue()
    file.put(arbre)
    resultat = []
    while file.empty() is False :
        element = file.get()
    if element is not None :
        print("L'arbre ou le sous arbre est : ",element)
    resultat.append(element.get_racine())
    print(resultat)
    file.put(element.get_gauche())
    file.put(element.get_droite())
    return resultat

print("---------- C'est la BFS (Breadth First Search), parcours en largeur d’abord ----------")
print("Le parcours en largeur d’abord de l'arbre donne la liste suivante : ",BFS(arbr)) 
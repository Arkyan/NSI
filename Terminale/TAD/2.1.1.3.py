"""Implémentation de type abstrait Liste en utilisant le type natif list de Python
Liste désigne la structure de données que nous utilisions pour gérer les listes.
Elt désigne la structure de données pouvant etre un élément de nos liste.
Description rapide de l'interface :
-----------------------------------
1 ::: nouvelleListe() -> Liste
2 ::: estVide(liste:Liste) -> bool
3 ::: compteListe(liste:Liste) -> int
4 ::: afficherListe(liste:Liste) -> str
5 ::: insererElement(x:Elt, liste:Liste, position:int) -> Liste
7 ::: supprimerElement(liste:Liste, position:int) -> Liste
"""

def nouvelleListe() :
    """Renvoie une liste vide
    :: reutrn (Liste) :: renvoie une liste vide sous forme d'un tableau vide
    """
    return ()

def estVide(lst) :
    """Renvoie True si la liste est vide
    :: param lst(Liste) :: une liste à tester
    :: return (bool) :: True si la liste est vide
    """
    if len(lst) == 0 :
        print("Attention la liste est vide")
        return True
    return False

def compteListe(lst) :
    """Renvoie la taille de la lsite
    :: param lst(Liste) :: une liste
    """
    return len(lst)

def afficherListe(lst):
    """Renvoie une représentation de la Liste sous forme d'une séquence commencant par la tête
    :: param lst(Liste) :: une liste
    :: return (str) :: un string représentant notre liste
    """
    return print(lst)

def lireElement(lst, position):
    """Renvoie la valeur stockée à la position voulue
    :: param lst(Liste) :: une liste
    :: param position(int) :: une valeur d'index valide pour cette liste
    :: return (Elt) :: la valeur voulue
    """
    if position >= 0 and position < len(lst):
        return lst[position]
    else:
        return None
    
def insererElement(x, lst, position):
    """Renvoie une Liste en insérant x à la position position.
    :: param x(Elt) :: l'élément à insérer, compatible avec la liste
    :: param lst(Liste) :: une liste
    :: return (Liste) :: la nouvelle liste"""

    list2 = list(lst)  # Copie à l'identique de la liste
    list2.insert(position, x)  # Insertion de l'élément à la position voulue
    return list2  # On renvoie la nouvelle liste

def supprimerElement(lst, position):
    """Renvoie une nouvelle liste où on a supprimé l'élément situé à la position fournie
    :: param lst(Liste) :: une liste
    :: param position(int) :: une valeur d'index valide pour cette liste
    :: return (Liste) :: la nouvelle liste
    """
    if position >= 0 and position < len(lst):
        return lst[:position] + lst[position+1:]
    else:
        return lst
    
print("Nouvelle liste")
liste4 = nouvelleListe()
print("La liste 4 contient : ", liste4)
print("la liste 4 est vide : ", estVide(liste4))
print()

print("Supprimer tete")
print("La liste 4 contient : ", liste4)
liste4 = supprimerElement(liste4, 0)
print("La liste 4 contient : ", liste4)
print("la liste 4 sans la tête est : ", liste4)
print()

print("Inserer tête")
liste4 = insererElement(5, liste4, 0)
print("La liste 4 contient : ", liste4)
print("la liste 4 est vide : ", estVide(liste4))
print("La tête de la liste est : ", lireElement(liste4, 0))

print()

print("Inserer tête")
liste4 = insererElement(2, liste4, 0)
print("La liste 4 contient : ", liste4)
print("la liste 4 est vide : ", estVide(liste4))
print("La tête de la liste est : ", lireElement(liste4, 0))

print()

print("Inserer tête")
liste4 = insererElement(8, liste4, 0)
print("La liste 4 contient : ", liste4)
print("la liste 4 est vide : ", estVide(liste4))
print("La tête de la liste est : ", lireElement(liste4, 0))

print()

print("Inserer tête")
liste4 = insererElement(15, liste4, 0)
print("La liste 4 contient : ", liste4)
print("la liste 4 est vide : ", estVide(liste4))
print("La tête de la liste est : ", lireElement(liste4, 0))

print()

print("Inserer tête")
liste4 = insererElement(3, liste4, 0)
print("La liste 4 contient : ", liste4)
print("la liste 4 est vide : ", estVide(liste4))
print("La tête de la liste est : ", lireElement(liste4, 0))

print()

print("Supprimer tete")
liste4 = supprimerElement(liste4, 0)
print("La liste 4 sans la tête est : ", liste4)
print("la liste 4 est vide : ", estVide(liste4))

print()

print("Ajouter un élément à une certaine position")
print("La liste 4 contient : ", liste4)
liste4 = insererElement(88, liste4, 2)
print("Après insertion la liste 4 contient : ", liste4)

print()

print("Supprimer un élément à une certaine position")
print("La liste 4 contient : ", liste4)
liste4 = supprimerElement(liste4, 3)
print("Après suppression la liste 4 contient : ", liste4)

print()

print("Le nombre d'éléments de la liste 4 est : ", compteListe(liste4))

print(afficherListe(liste4))
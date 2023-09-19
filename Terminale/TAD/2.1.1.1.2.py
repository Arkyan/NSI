"""Implémentation du type abstrait mliste en utilisant des tableaux statiques"""
def nouvelleListe():
    """Renvoie une liste vide
    :: return (Liste) :: renvoie une liste vide sous forme d'un tuple vide()
    """
    return ()

def estVide(lst) : 
    """Renvoie True si la liste est vide
    ::param lst(Liste) :: une liste à tester
    ::return (bool) :: True si la liste est un tuple vide()
    """
    if lst==None or len(lst)==0 :
        return True 
    return False 

def insererTete(x, lst):
    """Renvoie une nouvelle liste où x est la tête et liste la queue
    :: param x(Elt) :: un élément compatible avec votre liste qui devient la tête
    :: param lst(Liste) :: la liste qui va devenir la queue de la nouvelle
    :: return (Liste) :: la nouvelle liste
    """
    list2 = [None] * (len(lst) + 1)  # On crée une liste plus longue de 1
    for i in range(len(lst)):
        list2[i+1] = lst[i]  # Décalage vers la droite
    list2[0] = x  # On place la tête
    return list2  # On renvoie la nouvelle liste

def lireTete(lst):
    """Renvoie la tête de la liste, sans toucher à la liste elle-même
    :: param lst(Liste) :: la liste dont on désire lire la tête
    :: return (Elt) :: la tête voulue, None si la tête est vide"""
    if len(lst) > 0:
        return lst[0]  # la valeur envoyée est la première valeur de la liste
    else:
        return None

def supprimerTete(lst):
    """
    Renvoie une nouvelle liste où on a supprimé la tête de l'ancienne
    :: param lst(liste) :: la liste dont on supprime la tête
    :: return (Liste) :: la nouvelle liste
    """
    if len(lst) == 0:
        return []  # La liste envoyée est vide
    else:
        list2 = [None] * (len(lst) - 1)  # On crée une liste moins longue de 1
        for i in range(1, len(lst)):
            list2[i-1] = lst[i]  # Décalage vers la gauche
        return list2  # On renvoie la nouvelle liste

liste1 =  []
liste2 = None
liste3 = "c"
print("La liste 1 contient : ", liste1)
print("la liste 1 est vide : ",estVide(liste1))
print("La liste 2 contient : ",liste2)
print("la liste 2 est vide : ",estVide(liste2))
print("La liste 3 contient : ",liste3)
print("la liste 3 est vide : ",estVide(liste3))
print()
print("ATTENTION")
print("Seule la liste 4 respecte l'interface TAD")
print()
print("Nouvelle Liste")
liste4 = nouvelleListe()
print("La liste 4 contient : ", liste4)
print("la liste 4 est vide : ",estVide(liste4))
print("La tête de la liste est : ", lireTete(liste4))
print()
print("Supprimer Tete")
liste4 = supprimerTete(liste4)
print("La liste 4 sans la tête est : ",liste4)
print("la liste 4 contient : ", liste4)
print()
print("Inserer Tete")
liste4 = insererTete(5, liste4)
print("la liste 4 contient : ", liste4)
print("la liste 4 est vide : ", estVide(liste4))
print("La tête de la liste est : ", lireTete(liste4))
print("la liste 4 contient : ", liste4)
print()
print("Inserer Tete")
liste4 = insererTete(2,liste4)
print("la liste 4 contient : ", liste4)
print("la liste 4 est vide : ", estVide(liste4))
print("La tête de la liste est : ", lireTete(liste4))
print("la liste 4 contient : ", liste4)
print()
print("Inserer Tete")
liste4 = insererTete(8,liste4)
print("la liste 4 contient : ", liste4)
print("la liste 4 est vide : ", estVide(liste4))
print("La tête de la liste est : ", lireTete(liste4))
print("la liste 4 contient : ", liste4)
print()
print("Inserer Tete")
liste4 = insererTete(15,liste4)
print("la liste 4 contient : ", liste4)
print("la liste 4 est vide : ", estVide(liste4))
print("La tête de la liste est : ", lireTete(liste4))
print("la liste 4 contient : ", liste4)
print()
print("Inserer Tete")
liste4 = insererTete(3,liste4)
print("la liste 4 contient : ", liste4)
print("la liste 4 est vide : ", estVide(liste4))
print("La tête de la liste est : ", lireTete(liste4))
print("la liste 4 contient : ", liste4)
print()
print("Supprimer Tete")
liste4 = supprimerTete(liste4)
print("La liste 4 sans la tête est : ", liste4)
print("la liste 4 est vide : ", estVide(liste4))
print("La tête de la liste est : ", lireTete(liste4))
print("la liste 4 contient : ", liste4)
print()
print("Supprimer Tete")
liste4 = supprimerTete(liste4)
print("La liste 4 sans la tête est : ", liste4)
print("la liste 4 est vide : ", estVide(liste4))
print("La tête de la liste est : ", lireTete(liste4))
print("la liste 4 contient : ", liste4)
print()
print("Supprimer Tete")
liste4 = supprimerTete(liste4)
print("La liste 4 sans la tête est : ", liste4)
print("la liste 4 est vide : ", estVide(liste4))
print("La tête de la liste est : ", lireTete(liste4))
print("la liste 4 contient : ", liste4)
print()
print("Supprimer Tete")
liste4 = supprimerTete(liste4)
print("La liste 4 sans la tête est : ", liste4)
print("la liste 4 est vide : ", estVide(liste4))
print("La tête de la liste est : ", lireTete(liste4))
print("la liste 4 contient : ", liste4)
print()
print("Supprimer Tete")
liste4 = supprimerTete(liste4)
print("La liste 4 sans la tête est : ", liste4)
print("la liste 4 est vide : ", estVide(liste4))
print("La tête de la liste est : ", lireTete(liste4))
print("la liste 4 contient : ", liste4)
#------------------------------------------------------------------------------


def lireElement(lst, position) :
    """Renvoie la valeur stockée à la position voulue
    :: param lst(liste) :: une liste
    :: param position(int) :: une valeur d'index valide pour cette liste
    :: return (Elt) :: la valeur voulue """
    return lst[position]

def insererElement(x, lst, position):
    """Renvoie une liste en insérant x à la position position
    :: param x(ELt) :: l'élément à insérer, compatible avec la liste
    :: param lst(liste) :: une liste
    :: param position(int) :: une valeur d'index valide pour cette liste
    :: return (Liste) :: la nouvelle liste
    """
    list2 = [None] * (len(lst) + 1) # On crée une liste plus longue de 1
    for i in range(position): # Copie à l'identique jusqu'à la position
        list2[i] = lst[i]
    list2[position] = x # On place l'élément à sa position
    for i in range(position + 1, len(list2)): # Décalage vers la droite jusqu'à la fin
        list2[i] = lst[i - 1]
    return list2 # On renvoie la nouvelle liste

def supprimerElement(lst, position):
    """Renvoie une nouvelle liste où on a supprimé l'élément situé à la position fournie
    :: param lst(liste) :: une liste
    :: param position(int) :: une valeur d'index valide pour cette liste
    :: return (Liste) :: la nouvelle liste
    """
    list2 = [None] * (len(lst) - 1) # On crée une liste plus courte de 1
    for i in range(position): # Copie à l'identique jusqu'à la position
        list2[i] = lst[i]
    for i in range(position, len(lst) - 1): # Décalage vers la gauche jusqu'à la fin
        list2[i] = lst[i + 1]
    return list2 # On renvoie la nouvelle liste

def compteListe(lst) :
    return len(lst)
    
print("Nouvelle Liste")
liste4 = nouvelleListe()
print("La liste 4 contient : ", liste4)
print("la liste 4 est vide : ",estVide(liste4))
print("La tête de la liste est : ", lireTete(liste4))
print()
print("Supprimer Tete")
liste4 = supprimerTete(liste4)
print("La liste 4 sans la tête est : ",liste4)
print("la liste 4 contient : ", liste4)
print()
print("Inserer Tete")
liste4 = insererTete(5, liste4)
print("la liste 4 contient : ", liste4)
print("la liste 4 est vide : ", estVide(liste4))
print("La tête de la liste est : ", lireTete(liste4))
print("la liste 4 contient : ", liste4)
print()
print("Inserer Tete")
liste4 = insererTete(2,liste4)
print("la liste 4 contient : ", liste4)
print("la liste 4 est vide : ", estVide(liste4))
print("La tête de la liste est : ", lireTete(liste4))
print("la liste 4 contient : ", liste4)
print()
print("Inserer Tete")
liste4 = insererTete(8,liste4)
print("la liste 4 contient : ", liste4)
print("la liste 4 est vide : ", estVide(liste4))
print("La tête de la liste est : ", lireTete(liste4))
print("la liste 4 contient : ", liste4)
print()
print("Inserer Tete")
liste4 = insererTete(15,liste4)
print("la liste 4 contient : ", liste4)
print("la liste 4 est vide : ", estVide(liste4))
print("La tête de la liste est : ", lireTete(liste4))
print("la liste 4 contient : ", liste4)
print()
print("Inserer Tete")
liste4 = insererTete(3,liste4)
print("la liste 4 contient : ", liste4)
print("la liste 4 est vide : ", estVide(liste4))
print("La tête de la liste est : ", lireTete(liste4))
print("la liste 4 contient : ", liste4)
print()
print("Supprimer Tete")
liste4 = supprimerTete(liste4)
print("La liste 4 sans la tête est : ", liste4)
print("la liste 4 est vide : ", estVide(liste4))
print("La tête de la liste est : ", lireTete(liste4))
print("la liste 4 contient : ", liste4)
print("Ajouter un élément à une certaine position")
print("La liste 4 contient : ", liste4)
liste4 = insererElement(88,liste4,2)
print("Après insertion la liste 4 contient : ",liste4)
print()
print("Supprimer un élément à une certaine position")
print("la liste 4 contient : ", liste4)
liste4=supprimerElement(liste4,3)
print("Après suppression la liste 4 contient : ",liste4)
print()
print("Le nombre d'élément dans la liste 4 est : ",compteListe(liste4)) 


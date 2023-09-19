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

def insererTete(x,lst) :
    """Renvoie une nouvelle liste où x est la tête et liste la queue
    :: param x(Elt) :: un élément compatible avec votre liste qui devient la tête
    :: param lst(Liste) :: la liste qui va devenir la queue de la nouvelle
    :: return (Liste) :: la nouvelle liste
    """
    lst.insert(0,x)
    return (lst)

def lireTete(lst) :
    """Renvoie la tête de la liste, sans toucher à la liste elle-même
    :: param lst(Liste) :: la liste dont on désire lire la tête
    :: return (Elt) :: la tête voulue, None si la tête est vide"""
    if len(lst) != 0 :
        return lst[0]
    else :
        return None

def supprimerTete(lst):
    """
    Renvoie une nouvelle liste où on a supprimé la tête de l'ancienne
    :: param lst(liste) :: la liste dont on supprime la tête
    :: return (Liste) :: la nouvelle liste
    """
    if len(lst) == 0:
        return [] #la liste envoyée est vide
    else:
        return lst[1:] #la valeur envoyée est la deuxième partie du tuple

def afficherListe(lst):
    """
    Renvoie une représentation de la liste sous forme d'une séquence commençant par la tête
    :: param lst(Liste) :: une liste
    ::return liste(Liste) :: la liste
    """
    liste = []
    while lst:
        liste.append(lst[0])
        lst = lst[1:]
    return liste

def compteListe(lst) :
    return len(lst)

liste1 = () 
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
print("Seule la liste 4 respecte l'interface TAD : ")
print("Les listes 1 à 3 sont crées sans passer par la fonction nouvelleListe.")
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
print("La liste 4 convertie en type list est : ", afficherListe(liste4))
print()
print("Le nombre d'élémént dans la liste 4 est : ", compteListe(liste4))

def lireElement(lst, position):
    """Renvoie la valeur d'un élément à une certaine position de la liste
    :: param lst(Liste) :: une liste
    :: param position(int) :: une valeur de position valide pour cette liste
    :: return (Elt) :: la valeur située à cette position 
    """
    for i in range(position + 1):
        return lst[position]

def insererElement(x, lst, position):
    """Renvoie une représentation de la Liste contenant le
    nouvel élément sous forme d'une séquence commençant par la tête
    :: param x(Elt) :: l'élement à insérer, compatible avec la liste
    :: param lst(Liste) :: une liste
    :: param position(int) :: une valeur d'index valide pour cette liste 
    :: return(Liste) :: la nouvelle liste
    """
    lesTetes = lst[:position]
    for i in range(position, len(lst)):
        lst[i], x = x, lst[i]
    lst.append(x)
    return lesTetes + [x] + lst[position+1:]

def supprimerElement(lst, position):
    """Renvoie une représentation de la Liste ne contenant plus l'élement
    supprimer sous forme d'une séquence commençant par la tête
    :: param lst(Liste) :: une liste
    :: param position(int) :: une valeur d'index valide pour cette liste
    :: return (Liste) :: la nouvelle liste
    """
    lesTetes = lst[:position]
    for i in range(position+1, len(lst)):
        lesTetes.append(lst[i])
    return lesTetes

for i in range (len(afficherListe(liste4))) :
    print("La valeur en position", i ," est :", lireElement(liste4,i))

print()
print("Ajouter un élément à une certaine position")
print("La liste 4 contient : ", liste4)
liste4=insererElement(88,liste4,2)
print("Après insertion la liste 4 contient : ", liste4)
print()
print("Supprimer un élement à une certaine position")
print("La liste 4 contient : ", liste4)
liste4=supprimerElement(liste4,3)
print("Après suppression la liste 4 contient : ",liste4)
print()
print("La liste 4 convertie en type list est : ", afficherListe(liste4))
print()
print("Le nombre d'élements dans la liste 4 est : ", compteListe(liste4))


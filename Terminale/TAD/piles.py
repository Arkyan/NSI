def pile() :
    #retourne une liste vide
    return []

def vide(p) :
    """
    Renvoie True si la pile est vide, False sinon
    """
    return p == []

def empiler(p, x) :
    """Ajoute l'élément x à la pile p"""
    p.append(x)

def depiler(p) :
    """Si la pile n'est pas vide, dépile l'élément du sommet de la pile p sinon averti l'utilisateur que la pile est vide (voir le cours sur les assertions de premiere)
    """
    try:
        return p.pop()
    except IndexError:
        print("Attente votre pile est vide, vous ne pouvez plus dépiler")
        return None

def taille(p) :
    """retourne la taille de la pile"""
    if len(p) == 0:
        return 0
    else:
        return len(p)
    
def sommet(p) :
    """retourne le sommet de la pile sans le supprimer"""
    if vide(p):
        return None
    else:
        return p[-1]
    
pil = pile()
print(pil)
print("La taille de la pile est : ", taille(pil))
print("A ce niveau la pile est vide : ", vide(pil))
print("Le sommet de la pile est : ", sommet(pil))

for i in range(5) :
    print("Empiler")
    empiler(pil, i)
    print(pil)
    print("La taille de la pile est : ", taille(pil))
    print("A ce niveau la pile est vide : ", vide(pil))
    print("Le sommet de la pile est : ", sommet(pil))

for i in range(6) :
    print("Depiler")
    pil = depiler(pil)
    print(pil)
    print("La taille de la pile est : ", taille(pil))
    print("A ce niveau la pile est vide : ", vide(pil))
    print("Le sommet de la pile est : ", sommet(pil))
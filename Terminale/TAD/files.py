def file() :
    #retourne une liste vide
    return []

def vide(f) :
    """Renvoie True si la file est vide et False sinon"""
    return f == []

def enfiler(f, x) :
    """Ajoute l'élément x à la file f"""
    f.append(x)
    
def defiler(f) :
    """Si la file n'est pas vide, défile le premier élément de
    la file f sinon averti l'utilisateur que la file est vide
    (voir le cours sur les assertions de premiere)"""
    try :
        element = f.pop(0)
        return element
    except IndexError :
        print("La file est vide")
        return None
    
def taille(f) :
    """retourne la taille de la file"""
    if vide(f) :
        return 0
    else :
        return len(f)
    
def sommet(f) :
    """retourne le sommet de la file sans le supprimer"""
    if vide(f) :
        return None
    else :
        return f[0]
    
fil = file()
print(fil)
print("La taille de la file est : ", taille(fil))
print("A ce niveau la file est vide : ", vide(fil))
print("Le somme tde la file est : ", sommet(fil))

for i in range(5) :
    print("Enfiler")
    enfiler(fil, 3*i)
    print(fil)
    print("la taille de la file est : ", taille(fil))
    print("A ce niveau la file est vide : ", vide(fil))
    print("Le sommet de la file est : ", sommet(fil))

for i in range(6) :
    print("Défiler")
    defiler(fil)
    print(fil)
    print("La taile de la file est : ", taille(fil))
    print("A ce niveau la file est vide : ", vide(fil))
    print("Le sommet de la file est : ", sommet(fil))
    
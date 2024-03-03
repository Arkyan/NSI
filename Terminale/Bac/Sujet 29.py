#Exo 1
class Arbre:
    def __init__(self, etiquette):
        self.v = etiquette
        self.fg = None
        self.fd = None


def taille(a):
    if a == None:
        return 0
    return 1+taille(a.fg)+taille(a.fd)

def hauteur(a):
    if a == None:
        return 0
    return 1+max(hauteur(a.fg), hauteur(a.fd))

abr = Arbre(0)
a1 = Arbre(1)
a3 = Arbre(3)
a2 = Arbre(2)
a4 = Arbre(4)
a5 = Arbre(5)
a6 = Arbre(6)

a4.fd = a6
a2.fg = a4
a2.fd = a5
a1.fg = a3
abr.fg = a1
abr.fd = a2



#Exo 2
def ajoute(indice, element, liste):
    nbre_elts = len(liste)
    L = [0 for i in range(nbre_elts + 1)]
    if indice <  nbre_elts:
        for i in range(indice):
            L[i] = liste[i]
        L[indice] = element
        for i in range(indice + 1, nbre_elts + 1):
            L[i] = liste[i-1]
    else:
        for i in range(nbre_elts):
            L[i] = liste[i]
        L[nbre_elts] = element
    return L

print(ajoute(1, 4, [7, 8, 9]))
assert ajoute(1, 4, [7, 8, 9]) == [7, 4, 8, 9]

print(ajoute(3, 4, [7, 8, 9]))
assert ajoute(3, 4, [7, 8, 9]) == [7, 8, 9, 4]

print(ajoute(4, 4, [7, 8, 9]))
assert ajoute(4, 4, [7, 8, 9]) == [7, 8, 9, 4]
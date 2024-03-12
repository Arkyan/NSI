#Exo 1
class Arbre:
    def __init__(self, etiquette):
        self.v = etiquette
        self.fg = None
        self.fd = None

def taille(a):
    if a is None:
        return 0
    if (a.fg is None) and (a.fd is None):
        return 1
    else:
        return 1 + taille(a.fg) + taille(a.fd)

a = Arbre(1)
a.fg = Arbre(4)
a.fd = Arbre(0)
a.fd.fd = Arbre(7)

print("taille(None) =", taille(None))
print("taille(Arbre(1)) =", taille(Arbre(1)))
print("taille(a) =", taille(a))

assert taille(None) == 0
assert taille(Arbre(1)) == 1
assert taille(a) == 4

print("--------------------")

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

print("ajoute(1, 4, [7, 8, 9])", ajoute(1, 4, [7, 8, 9]))
print("ajoute(3, 4, [7, 8, 9])", ajoute(3, 4, [7, 8, 9]))
print("ajoute(4, 4, [7, 8, 9])", ajoute(4, 4, [7, 8, 9]))

assert ajoute(1, 4, [7, 8, 9]) == [7, 4, 8, 9]
assert ajoute(3, 4, [7, 8, 9]) == [7, 8, 9, 4]
assert ajoute(4, 4, [7, 8, 9]) == [7, 8, 9, 4]
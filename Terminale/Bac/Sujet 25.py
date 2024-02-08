#Exo 1 
def enumere(L):
    d = {}
    for i in range(len(L)):
        if L[i] in d :
            d[L[i]].append(i)
        else :
            d[L[i]]=[i]
    return d


print("enumere([1, 1, 2, 3, 2, 1]) =", enumere([1, 1, 2, 3, 2, 1]))

assert enumere([1, 1, 2, 3, 2, 1]) == {1: [0, 1, 5], 2: [2, 4], 3: [3]}

print("---------------------------------")

#Exo 2 
class Arbre:
    def __init__(self, etiquette):
        self.v = etiquette
        self.fg = None
        self.fd = None

def parcours(arbre, liste):
    if arbre != None:
        parcours(arbre.fg, liste)
        liste.append(arbre.v)
        parcours(arbre.fd, liste)
    return liste

def insere(arbre, cle):
    if cle < arbre.v :
        if arbre.fg != None:
            insere(arbre.fg, cle)
        else:
            arbre.fg = Arbre(cle)
    else:
        if arbre.fd != None:
            insere(arbre.fd, cle)
        else:
            arbre.fd = Arbre(cle)

a = Arbre(5)
insere(a, 2)
insere(a, 3)
insere(a, 7)
l = []

print("parcours(a, l) =", parcours(a, l))
#assert parcours(a, l) == [2, 3, 5, 7]
#Exo 1 
def enumere(L):
    d = {}
    for i in range(len(L)):
        if L[i] in d :
            d[L[i]].append(i)
        else :
            d[L[i]]=[i]
    return d




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

Abr = Arbre(5)
a1 = Arbre(2)
a2 = Arbre(3)
a3 = Arbre(7)

Abr.fg = a1
Abr.fd = a3
Abr.fg.fd = a2 

insere(Abr, 1)
insere(Abr, 4)
insere(Abr, 6)
insere(Abr, 8)

print(parcours(Abr, []))
#Exo 1
class ABR:
    def __init__(self, g0, v0, d0):
        self.gauche = g0
        self.cle = v0
        self.droit = d0
    def __repr__(self):
        return f"({self.gauche}, {self.cle}, {self.droit})"

        

n0 = ABR(None,0,None)
n3 = ABR(None,3,None)
n2 = ABR(None,2,n3)
abr1 = ABR(n0,1,n2)

abr = ABR(ABR(None, 0, None), 1, ABR(None, 2, ABR(None, 3, None)))
print("abr =", abr)

def ajoute(cle, a):
    if a is None:
        return ABR(None, cle, None)
    elif cle == a.cle:
        return a
    elif cle < a.cle:
        return ABR(ajoute(cle, a.gauche), a.cle, a.droit)
    else:
        return ABR(a.gauche, a.cle, ajoute(cle, a.droit))

print("ajoute(4,abr) =", ajoute(4,abr))
print("ajoute(-5, abr) =", ajoute(-5,abr))
print("ajoute(2, abr) =", ajoute(2,abr))

print('------------------')


#Exo 2
def empaqueter(liste_masses, c):
    n = len(liste_masses)
    nb_boites = 0
    boites = [0]*n
    for masse in liste_masses :
        i=0
        while i <= nb_boites and boites[i] + masse > c:
                i = i + 1
        if i == nb_boites + 1:
                nb_boites = nb_boites + 1
        boites[i] = boites[i] + masse
    return nb_boites + 1

print("empaqueter([1, 5, 2], 5) =", empaqueter([1, 5, 2], 5))
print("empaqueter([7, 6, 3, 4, 8, 5, 9, 2], 11) =", empaqueter([7, 6, 3, 4, 8, 5, 9, 2], 11))

assert empaqueter([1, 5, 2], 5) == 2
assert empaqueter([7, 6, 3, 4, 8, 5, 9, 2], 11) == 5

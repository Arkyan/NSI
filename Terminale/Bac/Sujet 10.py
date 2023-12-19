#Exo 1 
def maxliste(tab):
    maxi = tab[0]
    for v in tab:
        if v > maxi:
            maxi = v
    return maxi

#Exo 2
class Pile:
    def __init__(self):
        self.valeurs = []

    def est_vide(self):
        return self.valeurs == []

    def empiler(self, c):
        self.valeurs.append(c)

    def depiler(self):
        if self.est_vide() == False:
            self.valeurs.pop()


def parenthesage(ch):
    p = Pile()
    for c in ch:
        if c == "(":
            p.empiler(c)
        elif c == ")":
            if p.est_vide():
                return False
            else:
                p.depiler()
    return p.est_vide()
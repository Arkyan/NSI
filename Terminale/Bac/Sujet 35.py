#Exo 1
a = [1, 0, 1, 0, 1, 1, 0, 1]
b = [0, 1, 1, 1, 0, 1, 0, 0]
c = [1, 1, 0, 1]
d = [0, 0, 1, 1]
def ou_exclusif(t1, t2):
    n = len(t1)
    t = [0]*n
    for i in range(n):
        if t1[i] == t2[i]:
            t[i] = 0
        else :
            t[i] = 1
    return t

print(ou_exclusif(a, b))
print(ou_exclusif(c, d))
assert ou_exclusif(a, b) == [1, 1, 0, 1, 1, 0, 0, 1]
assert ou_exclusif(c, d) == [1, 1, 1, 0]

print("-----------------------------")

#Exo 2
c2 = [[1, 7], [7, 1]]
c3 = [[3, 4, 5], [4, 4, 4], [5, 4, 3]]
c3bis = [[2, 9, 4], [7, 0, 3], [6, 1, 8]]


class Carre:
    def __init__(self, liste, n):
        self.ordre = n
        self.tableau = [[liste[i + j * n] for i in range(n)] for j in range(n)]

    def affiche(self):
        for i in range(self.ordre):
            print(self.tableau[i])

    def somme_ligne(self, i):
        somme = 0
        for j in range(self.ordre):
            somme = somme + self.tableau[i][j]
        return somme

    def somme_col(self, j):
        somme = 0
        for i in range(self.ordre):
            somme = somme + self.tableau[i][j]
        return somme

    def est_semimagique(self):
        s = self.somme_ligne(0)

        for i in range(1, self.ordre):
            if self.somme_ligne(i) != s:
                return False

        for j in range(self.ordre):
            if self.somme_col(j) != s:
                return False

        return True

liste = (3, 4, 5, 4, 4, 4, 5, 4, 3)
c3t = Carre(liste, 3)
c3t.affiche()
print(c3t.est_semimagique())

##########################################################

c2 = [[1, 7], [7, 1]]
c3 = [[3, 4, 5], [4, 4, 4], [5, 4, 3]]
c3bis = [[2, 9, 4], [7, 0, 3], [6, 1, 8]]

c2_class = Carre([1, 7, 7, 1], 2)
c3_class = Carre([3, 4, 5, 4, 4, 4, 5, 4, 3], 3)
c3bis_class = Carre([2, 9, 4, 7, 0, 3, 6, 1, 8], 3)

print("c2_class.est_semimagique() =", c2_class.est_semimagique())
print("c3_class.est_semimagique() =", c3_class.est_semimagique())
print("c3bis_class.est_semimagique() =", c3bis_class.est_semimagique())

assert c2_class.est_semimagique() == True
assert c3_class.est_semimagique() == True
assert c3bis_class.est_semimagique() == False 
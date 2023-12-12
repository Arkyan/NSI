#Exo 1
def ou_exclusif(t1, t2):
    n = len(t1)
    t = [0]*n
    for i in range(n):
        if t1[i] == t2[i]:
            t[i] = 0
        else :
            t[i] = 1
    return t

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
    
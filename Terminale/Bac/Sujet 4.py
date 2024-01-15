#Exo 1 
def a_doublon(tab):
    n = len(tab)
    if n < 2 :
        return False
    for i in range(n-1):
        if tab[i] == tab[i+1]:
            return True
    return False

print("a_doublon([]) = ", a_doublon([]))
print("a_doublon([1]) = ", a_doublon([1]))
print("a_doublon([1, 2, 4, 6, 6]) = ", a_doublon([1, 2, 4, 6, 6]))
print("a_doublon([2, 5, 7, 7, 7, 9]) = ", a_doublon([2, 5, 7, 7, 7, 9]))
print("a_doublon([0, 2, 3]) = ", a_doublon([0, 2, 3]))

assert a_doublon([]) == False
assert a_doublon([1]) == False
assert a_doublon([1, 2, 4, 6, 6]) == True
assert a_doublon([2, 5, 7, 7, 7, 9]) == True
assert a_doublon([0, 2, 3]) == False

print("----------------------------------------")

#Exo 2
def voisinage(n, ligne, colonne):
    voisins = []
    for l in range(max(0,ligne-1), min(n, ligne+2)):
        for c in range(max(0, colonne-1), min(n, colonne+2)):
            if (l, c) != (ligne, colonne):
                voisins.append((l,c))
    return voisins

def incremente_voisins(grille, ligne, colonne):
    voisins = voisinage(len(grille), ligne, colonne)
    for l, c in voisins:
        if grille[l][c] != -1:
            grille[l][c] = grille[l][c] + 1

def genere_grille(bombes):
    n = len(bombes)
    grille = [[0 for colonne in range(n)] for ligne in range(n)]
    for ligne, colonne in bombes:
        grille[ligne][colonne] = -1
        incremente_voisins(grille, ligne, colonne)
    return grille

print("genere_grille(([(1, 1), (2, 4), (3, 1), (3, 3), (4, 4)]) = ", genere_grille(([(1, 1), (2, 4), (3, 1), (3, 3), (4, 4)])))
assert genere_grille(([(1, 1), (2, 4), (3, 1), (3, 3), (4, 4)])) == [[1, 1, 1, 0, 0], [1, -1, 1, 1, 1], [2, 2, 3, 2, -1], [1, -1, 2, -1, 3], [1, 1, 2, 2, -1]]


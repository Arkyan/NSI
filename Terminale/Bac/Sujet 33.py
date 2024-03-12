"""
Exercice N°1
"""

print("\033[92mExercice N°1\033[0m")

a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], 'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], 'H':['','']}

def taille(arbre, lettre):
    fils_gauche = arbre[lettre][0]
    fils_droit = arbre[lettre][1]

    if fils_gauche != '' and fils_droit != '':
        return 1 + taille(arbre, fils_gauche) + taille(arbre, fils_droit)

    if fils_gauche != '' and fils_droit == '':
        return 1 + taille(arbre, fils_gauche)

    if fils_gauche == '' and fils_droit != '':
        return 1 + taille(arbre, fils_droit)

    else:
        return 1

print("taille(a, 'F') ->", taille(a, 'F'))

assert taille(a, 'F') == 9

print()

"""
Exercice N°2
"""

print("\033[92mExercice N°2\033[0m")

def tri_selection(tab):
    N = len(tab)
    for k in range(N):
        imin = k
        for i in range(k+1, N):
            if tab[i] < tab[imin] :
                imin = i
        tab[k] , tab[imin] = tab[imin] , tab[k]

liste = [41, 55, 21, 18, 12, 6, 25]

tri_selection(liste)
print("liste ->", liste)

assert liste == [6, 12, 18, 21, 25, 41, 55]
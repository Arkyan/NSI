print("\033[92mExercice N°1\033[0m")
def moyenne (tab):
    moy = 0
    for i in range(len(tab)):
        moy += tab[i]
    return moy / len(tab)


print("moyenne([1]) =", moyenne([1]))
print("moyenne([1, 2, 3, 4, 5, 6, 7]) =", moyenne([1, 2, 3, 4, 5, 6, 7]))
print("moyenne([1, 2]) =", moyenne([1, 2]))

assert moyenne([1]) == 1
assert moyenne([1, 2, 3, 4, 5, 6, 7]) == 4
assert moyenne([1, 2]) == 1.5

print()

"""
Exercice N°2
"""

print("\033[92mExercice N°2\033[0m")

def dichotomie(tab, x):
    if len(tab) == 0:
        return False, 1
    if (x < tab[0]) or (x > tab[len(tab)-1]):
        return False, 2
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut + fin) // 2
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m - 1
    return False, 3

print("dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 28) =", dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 28))
print("dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 27) =", dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 27))
print(" dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 1) =", dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 1))
print("dichotomie([], 28) =", dichotomie([], 28))

assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 28) == True
assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 27) == (False, 3)
assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 1) == (False, 2)
assert dichotomie([], 28) == (False, 1)
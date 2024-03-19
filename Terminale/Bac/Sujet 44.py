#Exo 1
def renverse(mot):
    renv = ''
    for c in mot:
        renv = c + renv
    return renv

print("renverse('informatique') =", renverse('informatique'))
assert renverse('informatique') == 'euqitamrofni'


#Exo 2
def crible(n):
    premiers = []
    tab = [True] * n
    tab[0], tab[1] = False, False
    for i in range(2, n):
        if tab[i] == True:
            premiers.append(i)
            for multiple in range(2 * i, n, i):
                tab[multiple] = False
    return premiers

print("crible(40) =", crible(40))
assert crible(40) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
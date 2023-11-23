#Exo 1
def max_et_indice(tab):
    """
    Prend en paramÃ¨tre une liste non vide tab de nombres entiers 
    et renvoie la valeur du plus grand Ã©lÃ©ment de cette liste 
    ainsi que lâ€™indice de sa premiÃ¨re apparition dans cette liste.
    """
    index_m = 0
    maxi = tab[0]
    for i in range(1, len(tab)):
        if tab[i] > maxi:
            index_m = i
            maxi = tab[i]
    return maxi, index_m

print(max_et_indice([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]))
print(max_et_indice([-2]))
print(max_et_indice([-1, -1, 3, 3, 3]))
print(max_et_indice([1, 1, 1, 1]))
assert max_et_indice([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]) == (9, 3)
assert max_et_indice([-2]) == (-2, 0)
assert max_et_indice([-1, -1, 3, 3, 3]) == (3, 2)
assert max_et_indice([1, 1, 1, 1]) == (1, 0)

#Exo 2
def est_un_ordre(tab):
    for i in range(1, len(tab)+1):
        if i not in tab :
            return False
    return True


def nombre_points_rupture(ordre):
    assert est_un_ordre(ordre) 
    n = len(ordre)
    nb = 0
    if ordre[0] != 1: 
        nb = nb + 1
    i = 0
    while i < len(ordre)-1:
        if (ordre[i+1] - ordre[i]) not in [-1, 1]:
            nb = nb + 1
        i = i + 1
    if ordre[n-1] != n:
        nb = nb + 1
    return nb

print(est_un_ordre([1, 6, 2, 8, 3, 7]))
print(est_un_ordre([5, 4, 3, 6, 7, 2, 1, 8, 9]))
print(nombre_points_rupture([5, 4, 3, 6, 7, 2, 1, 8, 9]))
print(nombre_points_rupture([1, 2, 3, 4, 5]))
print(nombre_points_rupture([1, 6, 2, 8, 3, 7, 4, 5]))
print(nombre_points_rupture([2, 1, 3, 4]))
assert est_un_ordre([1, 6, 2, 8, 3, 7]) == False
assert est_un_ordre([5, 4, 3, 6, 7, 2, 1, 8, 9]) == True
assert nombre_points_rupture([5, 4, 3, 6, 7, 2, 1, 8, 9]) == 4
assert nombre_points_rupture([1, 2, 3, 4, 5]) == 0
assert nombre_points_rupture([1, 6, 2, 8, 3, 7, 4, 5]) == 7
assert nombre_points_rupture([2, 1, 3, 4]) == 2


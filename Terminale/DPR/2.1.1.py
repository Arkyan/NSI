list1 = [1,3,4,6,7,8,10,13,14]
elemt1 = 4
elemt2 = 5

def recherche_dichotomie_iterative(liste, element):
    debut = 0
    fin = len(liste) - 1
    while debut <= fin:
        milieu = (debut + fin) // 2
        if liste[milieu] == element:
            return True
        elif liste[milieu] > element:
            fin = milieu - 1
        else:
            debut = milieu + 1
    return False

print (elemt1,"est dans la liste triée ",list1, " par recherche itérative : ", recherche_dichotomie_iterative(list1,elemt1))
print (elemt2,"est dans la liste triée ",list1, " par recherche itérative : ", recherche_dichotomie_iterative(list1,elemt2))
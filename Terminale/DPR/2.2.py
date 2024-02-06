list1 = [1,3,4,6,7,8,10,13,14]
elemt1 = 4
elemt2 = 5

def recherche_dichotomie_recursive(liste, element):
    if len(liste) == 0:
        return False
    else:
        milieu = len(liste) // 2
        if liste[milieu] == element:
            return True
        elif liste[milieu] > element:
            return recherche_dichotomie_recursive(liste[:milieu], element)
        else:
            return recherche_dichotomie_recursive(liste[milieu+1:], element)
        
print (elemt1,"est dans la liste triée ",list1, " par recherche récursive : ", recherche_dichotomie_recursive(list1,elemt1))
print (elemt2,"est dans la liste triée ",list1, " par recherche récursive : ", recherche_dichotomie_recursive(list1,elemt2)) 
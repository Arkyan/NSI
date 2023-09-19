#Exo 1

def moyenne(tab):
    if tab == []:
        print('Le tableau donné est vide')
        return None
    else:
        somme = 0
        for elt in tab:
            somme += elt
        return somme / len(tab)

print("La moyenne est de :",moyenne([5,3,8]))
print("La moyenne est de :",moyenne([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print("La moyenne est de :",moyenne([]))


#Exo 2
def tri(tab):
    i= 0
    j= len(tab) - 1
    while i != j :
        if tab[i] == 0:
            i= i + 1
        else :
            valeur = tab[j]
            tab[j] = tab[i]
            tab[i] = valeur
            j= j - 1
    return tab

print("La fonction triée est :", tri([0, 1, 0, 1, 0, 1, 0, 1, 0]))

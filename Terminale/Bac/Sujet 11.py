#Exo 1
def convertir(tab):
    n = len(tab)
    s = 0
    for i in range(n):
        s = s + tab[i]*2**(n-i-1)
    return s

print("La conversion est :", convertir([1, 0, 1, 0, 0, 1, 1]))
print("La conversion est :", convertir([1, 0, 0, 0, 0, 0, 1, 0]))

print("--------------------------")

#Exo 2
tab = [9, 5, 8, 4, 0, 2, 7, 1, 10, 3, 6]
def tri_insertion(tab):
    n = len(tab)
    for i in range(1, n):
        valeur_insertion = tab[i]
        # la variable j est utilisée pour déterminer où placer la valeur à insérer
        j = i
        # tant qu'on a pas trouvé la place de l'élément à insérer
        # on décale les valeurs du tableau vers la droite
        while j > 0 and valeur_insertion < tab[j-1]:
            tab[j] = tab[j-1]
            j = j - 1
        tab[j] = valeur_insertion
    return tab 

print("La liste triée est : ", tri_insertion(tab))
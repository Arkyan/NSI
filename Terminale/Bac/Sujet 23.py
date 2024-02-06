#Exo 1 
def selection_enclos(table_animaux, num_enclos):
    tab = []
    for d in table_animaux:
        if d['enclos'] == num_enclos:
            tab.append(d)
    return tab
    




#Exo 2
tab_a = [3, 3, 3, 9, 9, 9, 1, 1, 1, 7, 2, 2, 2, 4, 4, 4, 8, 8, 8, 5, 5, 5]

tab_b = [8, 5, 5, 5, 9, 9, 9, 18, 18, 18, 3, 3, 3]

tab_c = [5, 5, 5, 1, 1, 1, 0, 0, 0, 6, 6, 6, 3, 8, 8, 8]

def trouver_intrus(tab, g, d):
    if g == d:
        return tab[g]

    else:
        nombre_de_triplets = (d - g)// 3
        indice = g + 3 * (nombre_de_triplets // 2)
        if tab[indice]==tab[indice+1] :
            return trouver_intrus(tab,indice+3,d)
        else:
            return trouver_intrus(tab,g,indice)
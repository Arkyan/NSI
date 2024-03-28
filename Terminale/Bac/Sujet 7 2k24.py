def gb_vers_entier(tab):
    entier = 0
    for i in range(len(tab)):
        if tab[i]:
            entier += 2**(len(tab)-1-i)
    return entier

print(gb_vers_entier([True, False, True, False, False, True]))  # Output: 83

def tri_insertion(tab):
    for i in range(1, len(tab)):
        valeur_insertion = tab[i]
        j = i - 1
        while j >= 0 and tab[j] > valeur_insertion:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = valeur_insertion


tab = [20, 23, 13, 91]
tri_insertion(tab)
print(tab) 
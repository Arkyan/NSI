def indices_maxi(tab):
    t_maxi = []
    maxi = tab[0]
    n = len(tab)
    for i in range(1,n):
        if tab[i]>maxi:
            maxi = tab[i]
    for i in range(n):
        if tab[i] == maxi:
            t_maxi.append(i)
    return maxi, t_maxi

def positif(pile):
    pile_1 = list(pile)
    pile_2 = []
    while pile_1 != []:
        x = pile_1.pop()
        if x >= 0:
            pile_2.append(x)
    while pile_2 != []:
        x = pile_2.pop()
        pile_1.append(x)
    return pile_1
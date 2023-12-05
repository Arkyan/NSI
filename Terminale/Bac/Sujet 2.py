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

print(indices_maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]))
print(indices_maxi([7]))
assert indices_maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]) == (9, [3, 8])
assert indices_maxi([7]) == (7, [0])


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

print(positif([-1, 0, 5, -3, 4, -6, 10, 9, -8]))
print(positif([-2])) 
assert positif([-1, 0, 5, -3, 4, -6, 10, 9, -8]) == [0, 5, 4, 10, 9]
assert positif([-2]) == []

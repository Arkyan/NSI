#Exo 1
def recherche(a, tab):
    c = 0
    for v in tab:
        if v==a:
            c=c+1
    return c

print(recherche(5, []))
assert recherche(5, []) == 0

print(recherche(5, [-2, 3, 4, 8]))
assert recherche(5, [-2, 3, 4, 8]) == 0

print(recherche(5, [-2, 3, 1, 5, 3, 7, 4]))
assert recherche(5, [-2, 3, 1, 5, 3, 7, 4]) == 1

print(recherche(5, [-2, 5, 3, 5, 4, 5]))
assert recherche(5, [-2, 5, 3, 5, 4, 5]) == 3


#Exo 2
pieces = [1, 2, 5, 10, 20, 50, 100, 200]

def rendu_monnaie(somme_due, somme_versee):
    rendu = []
    a_rendre = somme_versee - somme_due
    i = len(pieces) - 1
    while a_rendre > 0 :
        if pieces[i] <= a_rendre :
            rendu.append(pieces[i])
            a_rendre = a_rendre - pieces[i]
        else :
            i = i - 1
    return rendu

print(rendu_monnaie(700, 700))
assert rendu_monnaie(700, 700) == []

print(rendu_monnaie(102, 500))
assert rendu_monnaie(102, 500) == [200, 100, 50, 20, 20, 5, 2, 1]
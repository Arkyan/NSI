#Exo 1
def recherche(caractere, chaine):
    n = 0
    for c in chaine:
        if c == caractere:
            n = n + 1
    return n

print(recherche('e', "sciences"))
print(recherche('i', "mississippi"))
print(recherche('a', "mississippi"))
assert(recherche('e', "sciences") == 2)
assert(recherche('i', "mississippi") == 4)
assert(recherche('a', "mississippi") == 0)

#Exo 2
valeurs = [100,50,20,10,5,2,1]

def rendu_glouton(a_rendre, rang):
    if a_rendre == 0:
        return []
    v = valeurs[rang]
    if v <= a_rendre :
        return [v] + rendu_glouton(a_rendre - v, rang)
    else :
        return rendu_glouton(a_rendre, rang+1)

print(rendu_glouton(67, 0))
print(rendu_glouton(291, 0))
print(rendu_glouton(291,1))
assert(rendu_glouton(67, 0) == [50, 10, 5, 2])
assert(rendu_glouton(291, 0) == [100, 100, 50, 20, 20, 1])
assert(rendu_glouton(291, 1) == [100, 100, 50, 20, 20, 1])



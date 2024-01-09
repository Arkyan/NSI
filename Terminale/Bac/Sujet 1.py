#Exo 1
def verifie(tab):
    n=len(tab)
    if n==1:
        return True
    for i in range(n-1):
        if tab[i]>tab[i+1]:
            return False
    return True


print("verifie([0, 5, 8, 8, 9]) =", verifie([0, 5, 8, 8, 9]))
print("verifie([8, 12, 4]) =", verifie([8, 12, 4]))
print("verifie([-1, 4]) =", verifie([-1, 4]))
print("verifie([5]) =", verifie([5]))

assert verifie([0, 5, 8, 8, 9]) == True
assert verifie([8, 12, 4]) == False
assert verifie([-1, 4]) == True
assert verifie([5]) == True



#Exo 2
urne = ['A', 'A', 'A','B', 'C', 'B', 'C','B', 'C', 'B']

def depouille(urne):
    resultat = {}
    for bulletin in urne:
        if bulletin in resultat:
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            resultat[bulletin]=1
    return resultat

def vainqueur(election):
    vainqueur = '' #cette variable ne sert Ã  rien
    nmax = 0
    for candidat in election:
        if election[candidat] > nmax :
            nmax = election[candidat]
            vainqueur = candidat #cette ligne ne sert Ã  rien !
    liste_finale = [nom for nom in election if election[nom] == nmax]
    return liste_finale

election = depouille(urne)
print(election)
assert election == {'A': 3, 'B': 4, 'C': 3}

print(vainqueur(election))
assert vainqueur(election) == ['B']
pile = []

def puissance_recursive(nbre, puis) :
    if puis == 0 :
        return 1
    else :
        resultat = nbre * puissance_recursive(nbre, puis - 1)
        pile.append(resultat)
        return resultat
    
puissance_recursive(2, 3)
print(pile)

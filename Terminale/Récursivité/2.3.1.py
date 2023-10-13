print("Ce programme permet de calculer la puissance d'un nombre sans utiliser l'opérateur **")
nbr = int(input("Entrez un nombre : "))
E = int(input("Entrez la puissance : "))

def puissance(nbr, E) :
    if E == 0 :
        return 1
    else :
        return nbr * puissance(nbr, E-1)

print("Le nombre ",nbr," à la puissance ", E, " est égal à : ", puissance(nbr, E))

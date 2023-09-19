def prix(nombreAdultes , nombreEnfants , nombreEtudiants) :
    prixtotal = 37 * nombreAdultes + 28 * nombreEnfants + 30 * nombreEtudiants
    return prixtotal

adultes = int(input("Saisissez le nombre d'adultes :"))
enfants = int(input("Saisissez le nombre d'enfants :"))
etudiants = int(input("Saisissez le nombre d'étudiants :"))
jourAnniv = int(input("Saisissez 1 si c'est un jour d'anniversaire ou 0 si ça ne l'est pas :"))
prixApayer = prix(adultes , enfants , etudiants)
if jourAnniv == 1:
    prixApayer = prix(adultes , enfants , etudiants) - (prixApayer*(10/100))
else :
    prixApayer = prix(adultes , enfants , etudiants)
print("Vous devez payer" , prixApayer , "euros.")
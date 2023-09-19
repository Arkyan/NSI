def eurosVersDollars(montant) :
    doll = montant*1.19 #Si 1€ = 1.19$
    print(montant,"€ donne", doll, "$ par la fonction eurosVersDollars")
    return doll 

def dollarsVersYuans(montant) :
    yua = montant*6.76 #Si 1$ = 6,76¥
    print(montant,"$ donne", yua, "¥ par la fonction dollarsVersYuans")
    return yua 

def eurosVersYuans (montant) :
    #Appel de la fonction eurosVersDollars
    montantDollars = eurosVersDollars(montant)
    #Appel de la fonction dollarsVersYuans
    montantYuans = dollarsVersYuans(montantDollars)
    return montantYuans

montantEuros = int(input("Saississez le montant en € à convertir en ¥ : "))
montantConvert = eurosVersYuans(montantEuros)
print(montantEuros,"€ donne",montantConvert, "¥ en utilisant les deux fonctions")
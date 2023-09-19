def eurosVersDollars(euros) :
    doll = euros*1.19 #Si 1€ = 1.19$
    print(euros,"€ donne", doll, "$ par la fonction eurosVersDollars")
    return doll 

def dollarsVersYuans(dollars) :
    yua = dollars*6.76 #Si 1$ = 6,76¥
    print(dollars,"$ donne", yua, "¥ par la fonction dollarsVersYuans")
    return yua 

def eurosVersYuans (montantEnEurosAConvertirEnYuan) :
    #Appel de la fonction eurosVersDollars
    montantDollars = eurosVersDollars(montantEnEurosAConvertirEnYuan)
    #Appel de la fonction dollarsVersYuans
    montantYuans = dollarsVersYuans(montantDollars)
    return montantYuans

montantEuros = int(input("Saississez le montant en € à convertir en ¥ : "))
montantConvert = eurosVersYuans(montantEuros)
print(montantEuros,"€ donne",montantConvert, "¥ en utilisant les deux fonctions")


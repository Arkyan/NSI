def eurosVersDollars(montant) :
    doll = montant*1.19 #Si 1€ = 1.19$
    print(montant,"€ donne", doll, "$ par la fonction eurosVersDollars")
    return doll 

montantEuros = int(input("Saississez le montant en € à convertir en $ : "))
montantConvert = eurosVersDollars(montantEuros)
print(montantEuros,"€ donne",montantConvert, "$")
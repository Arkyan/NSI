def eurosVersDollars(montant) :
    """Cette fonction convertit en dollars le montant saisi en euros et elle renvoie la valeur en dollars
    Par exemple : Si le montant est 1€ la fonction renvoie 1,19$
    Si le montant est de 2€ la fonction renvoie 2,38$..."""
    return montant*1.19 #Si 1€ = 1.19$

montantEuros = int(input("Saississez le montant en € à convertir en $ : "))
print(montantEuros,"€ donne",eurosVersDollars(montantEuros), "$")
def fibonacci(nbre) :
    if nbre == 0 :
        return 0
    elif nbre == 1 :
        return 1
    else :
        return fibonacci(nbre - 1) + fibonacci(nbre - 2)
    
nbre = int(input("Veuillez saisir le mois (rang de la suite de Fibonacci) puis validez avec <<Enter>> : "))
print("Le nombre de couples de lapins au", nbre, "ème mois est :", fibonacci(nbre))


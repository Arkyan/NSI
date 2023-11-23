def fibonacciProgDynamique(nombre):
    if nombre == 1 or nombre == 2:
        return 1
    stockage = [None] * (nombre + 1)
    stockage[1], stockage[2] = 1,1
    for i in range(3, nombre + 1):
        stockage[i] = stockage[i - 1] + stockage[i - 2]
    return stockage[nombre]
mois = int(input("Veuillez saisir le mois (rang de la suite de Fibonacci) puis validez avec <<Enter>> : "))
print("Le nombre de couples de lapins au", mois,"ème mois, est :", fibonacciProgDynamique(mois))   
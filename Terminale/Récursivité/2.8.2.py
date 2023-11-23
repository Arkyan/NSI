def fibonacciDyn(nbre,a,b):
    if nbre==1:
        return b
    return fibonacciDyn(nbre - 1,b,a+b)
def fibo(nombre):
    return fibonacciDyn(nombre,0,1)
mois = int(input("Veuillez saisir le mois (rang de la suite de Fibonacci) puis validez avec <<Enter>> : "))
print("Le nombre de couples de lapins au", mois,"ème mois, est :",fibo(mois)) 
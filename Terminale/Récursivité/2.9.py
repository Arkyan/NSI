def pair(nbre):
    if nbre == 0:
        return True
    else:
        return impair(nbre - 1)
def impair(nbre):
    if nbre == 0:
        return False
    else :
        return pair(nbre - 1)
nombre = int(input("Veuillez saisir un nombre entier pour tester sa parité puis validez avec <<Enter>> : "))
print("Le nombre", nombre,"est pair :", pair(nombre))
print("Le nombre", nombre,"est impair :", impair(nombre)) 
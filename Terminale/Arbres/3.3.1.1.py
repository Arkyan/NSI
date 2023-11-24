from queue import Queue
. . .
def BFS(arbre):
    file = Queue()
    file.put(arbre)
    resultat = []
    while file.empty() is False :
        element = file.get()
    if element is not None :
        print("L'arbre ou le sous arbre est : ",element)
    resultat.append(element.get_racine())
    print(resultat)
    file.put(element.get_gauche())
    file.put(element.get_droite())
    return resultat
. . .
print("---------- C'est la BFS (Breadth First Search), parcours en largeur d’abord ----------")
print("Le parcours en largeur d’abord de l'arbre donne la liste suivante : ",BFS(arbr)) 
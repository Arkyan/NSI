def premierexemplerecursif(nbreboucles) :
    if nbreboucles > 9 :
        print("Ceci est le dernier message de cet exemple récursif car la condition d'arrêt est atteinte")
        print("Le nombre de boucle est égal à : ", nbreboucles)
    else :
        print("Ceci est un exemple récursif")
        print("Le nombre de boucle est égal à : ", nbreboucles)
        nbreboucles += 1 
        premierexemplerecursif(nbreboucles)
premierexemplerecursif(1)

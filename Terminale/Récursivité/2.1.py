def premiermauvaisexemlerecursif(nbrboucle) :
    print("Ceci est un très mauvais exemple récursif")
    print("Le nombre de boucles est de : ", nbrboucle)
    nbrboucle += 1
    premiermauvaisexemlerecursif(nbrboucle)

premiermauvaisexemlerecursif(1)


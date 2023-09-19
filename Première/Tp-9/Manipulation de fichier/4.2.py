import os
fichierTexte = open("dataNombresMoy.txt", "r")
contenuFichier = fichierTexte.readlines()
print("Le fichier contient :", contenuFichier)
fichierTexte.close()

for i in range (0, len(contenuFichier)) :
    print("Le", i+1, "ème nombre est", contenuFichier[i])
total = 0

for i in range (0, len(contenuFichier)) : 
    total = total + int(contenuFichier[i])
print("Le total des notes est de : ",total)
moyenne = total/len(contenuFichier)
print("La moyenne des notes est de : ", moyenne)
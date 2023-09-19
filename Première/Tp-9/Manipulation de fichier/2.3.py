#Ouvrir le fichier data.txt en lecture
fichierTexte = open("data.txt" , "r")

#Afficher le contenu du fichier data.txt
contenu = fichierTexte.read()
print(contenu)

#Fermer le fichier data.txt
fichierTexte.close()

#Liste 2D
#Importation des bibliothèques
from tkinter import * 
#variables
lignes = 10
colonnes = 10
#liste 2D de nombres
nombre = [[(i+j*10)for i in range(colonnes)]for j in range(lignes)]
print(nombre)
for i in range (lignes) :
    for j in range(colonnes) :
        print(nombre[i][j])
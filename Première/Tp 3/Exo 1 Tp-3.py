#programme Entrée Sortie avec la console
from tkinter import *
from math import sqrt

# Invitation à saisir un nombre réel
nombre = float(input("veuillez saisir un nombre puis validez avec <<Enter>> :"))
nombre = sqrt(nombre)
#affichage d'un message dans la console 
print ("Vous avez saisi le nombre : " + str(nombre))
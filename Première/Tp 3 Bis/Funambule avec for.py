#9 Funambule exercice 2

# Importation des bibliothèques
from tkinter import *
import time

# Initialisation des variables
largeur = 600
hauteur = 500
pas_x = 20
pas_y = 40
diametreBouton = 12
rayonBouton = int(diametreBouton/2)
largeur_rectangle = 100
longueur_rectangle = 160
abscisse_depart = 70
ordonnee_depart = 30
diametre = 8
temps = 1
x=abscisse_depart-diametreBouton/2
y=ordonnee_depart-diametreBouton/2

# Fonction permettant de creer une temporisation
def temporisation():
    fenetre.update()
    time.sleep(temps)

# Fonction permettant de créer un disque vert
def creer_trace (x,y):
    trace = canevas.create_oval(x, y, x+diametreBouton, y+diametreBouton, outline="green",width=1,fill="green")
    canevas.pack()

# Fonction permettant de créer un rectangle
def creer_rectangle ():
    canevas.create_rectangle(abscisse_depart, ordonnee_depart, abscisse_depart+largeur_rectangle, ordonnee_depart+longueur_rectangle, outline="blue",width=1)
    canevas.pack()

# Programme principal
fenetre = Tk()

# Création de la fenêtre
fenetre.title(' Funambule ')

# Création d'un widget ('wi'ndows ga'dget's) Canvas (zone graphique)
canevas = Canvas(fenetre, width = largeur, height =hauteur, bg ="white")
canevas.pack()

# Création du rectangle
creer_rectangle()
temporisation()

# parcours du côté haut
for x in range (abscisse_depart-rayonBouton,largeur_rectangle+abscisse_depart,pas_x):
    creer_trace (x,y)
    temporisation()

# parcours du côté droit
for y in range (ordonnee_depart-rayonBouton+pas_y,longueur_rectangle+ordonnee_depart,pas_y):
    creer_trace (x,y)
    temporisation()

# parcours du côté bas
for x in range (largeur_rectangle+abscisse_depart-pas_x-rayonBouton,abscisse_depart-rayonBouton-pas_x,-pas_x):
    creer_trace (x,y)
    temporisation()

# parcours du côté gauche
for y in range (longueur_rectangle+ordonnee_depart-pas_y-rayonBouton,ordonnee_depart-rayonBouton,-pas_y):
    creer_trace (x,y)
    temporisation()

# fin du programme principal
fenetre.mainloop()
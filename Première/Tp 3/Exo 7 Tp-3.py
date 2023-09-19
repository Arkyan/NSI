from tkinter import * 
from math import *

taille = "600x200+100+300"
titre = "Fenêtre NSI : Bouton, étiquette, zone de saisie et console"
icone = "gateau.ico"
couleur = "ivory"

def creer_fenetre(fenetre, taille, titre, icone, couleur) :
    fenetre.geometry(taille)
    fenetre.title(titre)
    fenetre.iconbitmap(icone)
    fenetre.configure(bg=couleur)
    return fenetre

fenetre= Tk()
fenetre=creer_fenetre(fenetre,taille,titre,icone,couleur)

votrepoids = StringVar()
votrepoids = Entry(fenetre, width=60)
affichage = Label (fenetre, text="Saississez votre poids en kg")
affichage.pack()
votrepoids.insert(0,"")
votrepoids.pack()

votretaille = StringVar()
votretaille = Entry(fenetre, width=60)
affichage2 = Label (fenetre, text="Saississez votre taille en m")
affichage2.pack()
votretaille.insert(0,"")
votretaille.pack()


def valider() :
    global affichage3
    global affichage4
    taillle = float(votretaille.get()) * float(votretaille.get())
    masse = float(votrepoids.get())
    imc = masse / taillle
    imc = round (imc, 1)
    affichage4 = Label (fenetre, text = "Votre imc est de " + str(imc) )
    affichage4.pack()
    if imc < 18.5 :
        catégorie = "Vous êtes trop maigre"
    elif imc >= 18.5 and imc < 25.5 :
        catégorie = "Vous êtes de corpulence normale"
    elif imc >= 25 : 
        catégorie = "Vous êtes en surpoids"
    affichage3 = Label ( fenetre, text="Vous faites parties de la catégorie --->" + catégorie )
    affichage3.pack()

def terminer() : 
    affichage3.destroy()
    affichage4.destroy()


Valider = Button(fenetre, text="Valider", command=valider)
Valider.pack()
Terminer = Button(fenetre, text="Terminer", command=terminer)
Terminer.pack()
fenetre.mainloop()




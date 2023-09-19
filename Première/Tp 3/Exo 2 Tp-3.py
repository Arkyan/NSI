
from tkinter import *
taille = "600x200+100+300"
titre = "Fenêtre NSI : Bouton, étiquette, zone de saisie et console"
icone = "gateau.ico"
couleur = "ivory"

def valider() : 
    nombre = float(zoneDeSaisie.get())**2
    affichage = Label (fenetre, text= "Vous avez saisi le nombre : "+str(nombre))
    affichage.place(x=100, y=100)
    print ("Vous avez saisi le nombre : "+ str(nombre))

def creer_fenetre(fenetre, taille, titre, icone, couleur) :
    fenetre.geometry(taille)
    fenetre.title(titre)
    fenetre.iconbitmap(icone)
    fenetre.configure(bg=couleur)
    return fenetre
fenetre= Tk()
fenetre=creer_fenetre(fenetre,taille,titre,icone,couleur)
etiquette = Label(fenetre,text="Nombre")
etiquette.pack()
zoneDeSaisie = StringVar()
zoneDeSaisie = Entry(fenetre, width=60)
zoneDeSaisie.insert(0,"Saisir un nombre à la place de ce texte puis <<Valider>>")
zoneDeSaisie.pack()
monBouton = Button(fenetre, text="Valider", command=valider)
monBouton.pack()
fenetre.mainloop()
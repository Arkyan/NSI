from tkinter import *

taille="600x200+100+300"
titre="fenêtre NSI"
icone="gateau.ico"
couleur="ivory"

def creer_fenetre (fenetre, taille, titre, icone, couleur) :
    fenetre.geometry(taille)
    fenetre.title(titre)
    fenetre.iconbitmap(icone)
    fenetre.configure(bg=couleur)
    return fenetre

fenetre=Tk()
fenetre=creer_fenetre(fenetre, taille, titre, icone, couleur)
label = Label(fenetre, text="bonjour tout le monde", fg="magenta", font= ("Serif", 45))
label.pack(side="left")
fenetre.mainloop()
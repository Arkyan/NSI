#4soleillevant
from tkinter import * 
largeur = 300
hauteur = 300 
x = 10
y = 20
xsoleil = 100
ysoleil = 250
long_soleil = 100 #longueur du soleil
larg_soleil = 100 #largeur du soleil
def clic (event) : 
    canevas.move(soleil, 0, -10) #définition du mouvement du soleil à chaque clic
def clic2 (event) :
    canevas.coords (soleil,xsoleil,ysoleil,xsoleil+long_soleil, ysoleil+larg_soleil) #definition des coordonées du soleil sur la fenetre
fenetre = Tk()
fenetre.title('soleil levant') #nom de la fenetre
canevas = Canvas(fenetre, width=largeur, height = hauteur, bg ='blue') #défini la couleur du fond
soleil = canevas.create_oval (xsoleil, ysoleil, xsoleil+long_soleil, ysoleil+larg_soleil, outline="yellow", width=1 ,fill="yellow") #défini la couleur du soleil
canevas.pack()
canevas.bind("<Button-1>", lambda event : clic(event)) #défini que quand on clic cela fait l'évenement raccordé au clic qui fait monté le soleil
canevas.bind("<Leave>", lambda event : clic2(event)) #défini que quand on clic cela fait l'évenement raccordé au clic2 qui fait redescendre le soleil au moment de quitter la fenetre
fenetre.mainloop()
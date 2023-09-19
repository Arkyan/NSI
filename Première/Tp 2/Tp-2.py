largeur=500
hauteur=500
from tkinter import *
 
def rond (event): #Un argument est envoyé automatiquement à la fonction suite au can.bind(...), c'est
    global label
    label.destroy()
    x,y = event.x,event.y #une instance d'une classe qui fournit les coordonnées du clic dans le canvas
                          #par le biais de ses attributs x et y (le nom event est donné à l'argument
                          #conventionnellement
    canevas.create_oval(x,y,x,y, outline='red', width= 6) #on crée un cercle de centre les coordonnées du clic dans notre Canvas 
def leave (event):
    global label
    canevas.delete("all")
    label.destroy()
    label = Label (fenetre, text="Vous êtes guéri", font= ("Serif", 15))
    label.pack(side="bottom")

def enter (event):
    global label
    label.destroy()
    label = Label (fenetre, text="Varicelle, Cliquez ici pour l'attraper", font= ("Serif", 15))
    label.pack(side="bottom")

fenetre = Tk()
fenetre.title('Varicelle')
canevas = Canvas(fenetre, width= largeur, height = hauteur)
label = Label (fenetre, text="Varicelle, Cliquez ici pour l'attraper", font= ("Serif", 15))
label.pack(side="bottom")
canevas.bind("<Button-1>", rond) #on lie le clic gauche à la fonction "rond"
canevas.bind("<Leave>", lambda event : leave(event))
canevas.bind("<Enter>", lambda event : enter(event))
canevas.pack() 
fenetre.mainloop()

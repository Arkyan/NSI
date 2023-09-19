hauteur  = 500
largeur = 500
xcarré = 60
ycarré = 70
def enter (event) :
    canevas.create_rectangle (xcarré, ycarré, xcarré+50, ycarré+50, fill='red', outline= 'black', width=5)
def clic (event) :
    canevas.create_rectangle (xcarré, ycarré, xcarré+50, ycarré+50, fill='blue', outline= 'black', width=5)
def leave (event) :
    canevas.create_rectangle (xcarré, ycarré, xcarré+50, ycarré+50, fill='green', outline= 'black', width=5) 
from tkinter import * 
fenetre = Tk ()
fenetre.title('carré')
canevas = Canvas(fenetre, width=largeur, height = hauteur)
carré = canevas.create_rectangle (xcarré, ycarré, xcarré+50, ycarré+50, fill= 'red', outline= 'black', width=5) 
canevas.pack()
canevas.bind("<Enter>", lambda event : enter(event))
canevas.bind("<Button-1>", lambda event : clic(event))
canevas.bind("<Leave>", lambda event : leave(event))
fenetre.mainloop()
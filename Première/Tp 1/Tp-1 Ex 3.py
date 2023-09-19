from tkinter import *
largeur = 480
hauteur = 340
x = 10
y = 20
xoval = 150 
yoval = 220
long = 300
larg = 200
long_oval = 200
larg_oval = 100
fenetre = Tk()
fenetre.title('Dessin d\'un rectangle et d\'une ellipse')
canevas = Canvas(fenetre, width = largeur, height = hauteur, bg ='green')
canevas.pack(padx = 40,pady = 20)
canevas.create_rectangle(x,y,long,larg,outline="blue",width=6, fill="red")
canevas.create_oval(xoval,yoval, xoval+long_oval, yoval+larg_oval, outline="yellow", width=6,fill="black")
fenetre.mainloop()
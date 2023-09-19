from tkinter import * 
# Initialisation des variables

hauteur = 300
largeur = 600
x_fenetre = 50
y_fenetre = 100

def clic (event,canevas) :
    x,y=event.x, event.y
    canevas.create_text(x,y, text = "clic en\n(X,Y) = ("+str(x)+";"+str(y)+")")
    canevas.coords(axe_vertical,x,0,x,hauteur)
    canevas.coords(axe_horizontal,0,y,largeur,y)
    fenetre.update()
    print(fenetre.winfo_height(), fenetre.winfo_width())

fenetre = Tk()
fenetre.configure(bg='white')
fenetre.title ("Détection clic souris et mire")
fenetre.geometry("%dx%d%+d%+d" % (largeur,hauteur,x_fenetre, y_fenetre))
canevas = Canvas(fenetre, width = largeur, height = hauteur, bg ='white')
axe_vertical = canevas.create_line( largeur/2 , 0 , largeur/2 , hauteur , width=1 , fill='black' )
axe_horizontal = canevas.create_line( 0 , hauteur/2 , largeur , hauteur/2 , width=1 , fill='black' )
canevas.pack()
canevas.bind("<Button-1>", lambda event : clic (event,canevas))
fenetre.mainloop()
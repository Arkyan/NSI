from tkinter import *  
import time 
n = 0

fenetre= Tk()
canevas = Canvas(fenetre, width = 500, height = 500)    
canevas.create_rectangle (70, 30, 170, 190, outline = 'blue')  
fenetre.title ('Funambule')
canevas.pack()

#haut(-28) 1 et 3
canevas.create_oval(70, 30, 78, 38,  fill = "green", width = 1)
canevas.create_oval(98, 30, 106, 38,  fill = "green", width = 1)
canevas.create_oval(126, 30, 134, 38,  fill = "green", width = 1)
canevas.create_oval(154, 30, 162, 38,  fill = "green", width = 1)

#gauche (-40) 2 et 4
canevas.create_oval(70, 70, 78, 78,  fill = "green", width = 1)
canevas.create_oval(70, 110, 78, 118,  fill = "green", width = 1)
canevas.create_oval(70, 150, 78, 158,  fill = "green", width = 1)

#bas (-28) 1 et 3
canevas.create_oval(78, 181, 86, 189,  fill = "green", width = 1)
canevas.create_oval(106, 181, 114, 189,  fill = "green", width = 1)
canevas.create_oval(134, 181, 142, 189,  fill = "green", width = 1)

#droite (-40) 2 et 4
canevas.create_oval(161, 70, 169, 78, fill= "green", width = 1 )
canevas.create_oval(161, 110, 169, 118, fill= "green", width = 1 )
canevas.create_oval(161, 150, 169, 158, fill= "green", width = 1 )
canevas.create_oval(161, 181, 169, 189, fill= "green", width = 1 )

fenetre.mainloop()

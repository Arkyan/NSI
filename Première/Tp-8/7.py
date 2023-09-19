from tkinter import *
from math import * 
import numpy as np

nbJuges = 7
meilleurenote = 0
pirenote = 0
sommedesnotes = 0
moyennedesnotes = 0
variance = 0
ectartype = 0
arrondimoyennedesnotes = 0
arrondiecrattype = 0
nombrenote = 0
note = []

while nombrenote < 7 :
    note.append(float(input("Entrer des notes comprises entre 1 et 10 :")))
    nombrenote = nombrenote + 1

print("La liste des notes rentrées est :",note)
note.sort()
meilleurenote = note[6]
print("La meilleure note est :",meilleurenote)
pirenote = note[0]
print("La pire note est :",pirenote)

for i in note : 
    sommedesnotes = sommedesnotes + i

moyennedesnotes = sommedesnotes/nbJuges
print("La moyenne des notes est de :",moyennedesnotes)

print("L'écart-type des 7 notes est de :",str(np.std(note)))
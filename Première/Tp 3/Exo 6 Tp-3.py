from math import *

NbrNotes = int(input("Nombre de notes : "))
AllNotes = 0
last_note = 
a = 0 

while last_note > 0 :
    note = int(input("Note sur 20 : "))

    a = a + 1
    AllNotes = AllNotes + note
Moy = AllNotes/NbrNotes
Moy = round(Moy, 2)
print("La moyenne est de : "+ str(Moy))
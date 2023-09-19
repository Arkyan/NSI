#Importation des bibliothèques maths et matplotlib( tracer des graphiques )
from math import * 
import matplotlib.pyplot as plt

#Données de type 1
liste_x_1 = [1,3,8,13]
liste_y_1 = [30,27.2,37.6,40.7]

#Données de type 2
liste_x_2 = [2,3,10,7]
liste_y_2 = [33,26,39,35]
table = [['t1',1,30],['t1',3,27.2],['t1',8,37.6],['t1',13,40.7],['t2',2,33],['t2',3,26],['t2',10,39],['t2',7,35]]
cible = [7,28.4]
demidiag = 7
raycercle = 6.4
largcarre = 11 

#k plus proches voisins
k = 3
plt.axis([0,15,0,50]) #Attention [x1,x2,y1,y2]
plt.axis("equal")
plt.xlabel("Caractéristique 1")
plt.ylabel("Caractéristique 2")
plt.title("Représentation des deux types")
plt.grid()
plt.scatter(liste_x_1,liste_y_1, label = "type 1")
plt.scatter(liste_x_2,liste_y_2, label = "type 2")

#Représention de la cible 
plt.scatter(cible[0],cible[1],label='cible')

#Tracé un losange de centre la cible
x = [cible[0]+demidiag, cible[0],cible[0]-demidiag,cible[0],cible[0]+demidiag]
y = [cible[1], cible[1]+demidiag,cible[1],cible[1]-demidiag,cible[1]]
plt.plot(x,y)
plt.legend
plt.show()
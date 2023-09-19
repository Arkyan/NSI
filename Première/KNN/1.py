#importation des bibliothèques pandas (lecture de fichier csv) et matplolib(tracer des graphiques)
import pandas
import matplotlib.pyplot as plt 

#Lecture du fichier csv
iris = pandas.read_csv("Iris_csv.csv")

#abscisses des points correspondant à la longueur des pétales du fichier csv
x=iris.loc[:,"longueur_petale"]

#ordonnées des points correspondant à la longueur des pétales du fichier csv
y=iris.loc[:,"largeur_petale"]

#Couleurs des points correspondant aux codes espèces du fichier csv
codespece = iris.loc[:,"code_espece"]

#imposer l'égalité des échelles sur le 2 axes pour éviter la déformation du cercle 
plt.axis("equal")

#Tracer les différents points
#Vert pour les iris setosa
plt.scatter(x[codespece==0],y[codespece==0], color="green",label="Iris setosa")

#Rouge pour les iris virginica
plt.scatter(x[codespece==1],y[codespece==1], color="red",label="Iris virginica")

#Bleu pour les iris versicolor
plt.scatter(x[codespece==2],y[codespece==2], color="blue",label="Iris versicolor")

#Insérer la légende du graphique
plt.legend()

#Insérer le litre du graphique
plt.title("Caractéristiques des iris")

#Insérer le nom de l'axe des abscisses du graphique
plt.xlabel("Longueur des pétales des iris")

#Insérer le nom de l'axe des ordonnées du graphique
plt.ylabel("Largeur des pétales des iris")

#Afficher le graphique
plt.show()
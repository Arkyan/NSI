#importation des bibliothèques pandas (lecture de fichier csv) et matplolib(tracer des graphiques)
import pandas
import matplotlib.pyplot as plt 
from sklearn.neighbors import KNeighborsClassifier

#Valeurs
longinco = 6
larginco = 2
k_Voisins = 3

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

#Noir pour les iris inconnus
plt.scatter(longinco,larginco, color="black")

#Tracé un cercle de centre (2.5,0.7)de rayon 0.85
cercle = plt.Circle((longinco,larginco),radius=0.85, linewidth=1,color="black",fill=False)

#gcf = get the current figure / gca = get the current polar axes ; add_artiste = trace le cercle
plt.gcf().gca().add_artist(cercle)

#algo knn
#Liste des longueurs des pétales
print(list(x))
#Liste des largeurs des pétales
print(list(y))

#faire une liste des tuples composés des longueurs et des largeurs des pétales
#zip : permet de regrouper 2 listes sous la forme d'une liste de tuples
listuples = list(zip(x,y))
print(listuples)

#La méthode KNeighbors Classifier prend en paramètre le nombre de plus proches voisins 
model = KNeighborsClassifier(n_neighbors=k_Voisins)

#model.fit() permet d'associer les tuples présents dsans la liste listuples avec les codespece(0:"iris setosa",1:"iris versicolor" ou 2 :"iris verginica").
#Par exemple le premier tuple de la list listuple, (1.4,0.2) est associé au prmier codespece de la liste codespece(0), et ainsi de suite...
model.fit(listuples,codespece)

#model.predict() permet d'effectuer une prédiction pour un couple [longueur_petale,largeur_petale] dans l'exemple ci-dessus longinco = 2.5 et larginco = 0.7.
#La variable prediction contient alors le codespece trouvé par l'algo knn, la variable prediction est une liste qui contient un seul élément (le codespece), il est donc nécessaire
#d'écrire prediction[0] afin d'obtenir le codespce
prediction = model.predict([[longinco,larginco]])
print(prediction)
print(prediction[0])

#Affichage des résultats
txt="Espèce de l'inconnu : "
#Si le code de prediction est 0
if prediction[0] == 0 :
    #afficher setosa
    txt = txt + "setosa"

#Si le code de prediction est 1
if prediction[0] == 1 :
    #afficher versicolor
    txt = txt + "versicolor"

#Si le code de prediction est 2
if prediction[0] == 2 :
    #afficher virginica
    txt = txt + "virginica"

#Fixer les positions des informations relatives aux résulatas de la prédiction
plt.text(1,-0.4, f"Largeur du pétale :{larginco} cm longueur du pétale : {longinco} cm", fontsize = 12)
plt.text(1,-0.6, f"k plus proches voisins : {k_Voisins}",fontsize = 12)
plt.text(1,-0.8, txt, fontsize = 12)

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
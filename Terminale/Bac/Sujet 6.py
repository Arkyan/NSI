#Exo 1
def recherche(tab, n):
    indice = len(tab)
    for i in range(len(tab)):
        if tab[i] == n:
            indice = i
    return indice

print(recherche([5, 3], 1))
print(recherche([2, 4], 2))
print(recherche([2, 3, 5, 2, 4], 2))
print("------------------------------------------")
#Exo 2
from math import sqrt

def distance(point1, point2):
    """ Calcule et renvoie la distance entre deux points. """
    return sqrt((point1[0] - point2[0])**2 + ((point1[1] - point2[1]))**2)

def plus_courte_distance(tab, depart):
    """ Renvoie le point du tableau tab se trouvant à la plus courte distance du point depart."""
    point = tab[0]
    min_dist = distance(point, depart)
    for i in range (1, len(tab)):
        if distance(tab[i], depart) < min_dist:
            point = tab[i]
            min_dist = distance(tab[i], depart)
    return point

print(distance((1, 0), (5, 3)))
print(distance((1, 0), (0, 1)))
print("----------------------------------------------------")
print(plus_courte_distance([(7, 9), (2, 5), (5, 2)], (0, 0)))
print(plus_courte_distance([(7, 9), (2, 5), (5, 2)], (5, 2)))
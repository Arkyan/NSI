#Exo 1
from random import randint

def lancer(n):
    t = []
    for _ in range(n):
        t.append(randint(1,6))
    return t

    
def paire_6(tab) :
    n = 0
    for v in tab:
        if v == 6:
            n = n + 1
    return n >= 2

lancer1 = lancer(5)
print(paire_6(lancer1))


lancer2 = lancer(5)
print(paire_6(lancer2))

lancer3 = lancer(3)
print(paire_6(lancer3))


lancer4 = lancer(0)
print(paire_6(lancer4))




print("-----------------")
#Exo 2
img=[[20, 34, 254, 145, 6], [23, 124, 237, 225, 69], [197, 174, 207, 25, 87], [255, 0, 24, 197, 189]]

def nbLig(image):
    
    return len(image)

def nbCol(image):
 
    return len(image[0])

def negatif(image):
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))]

    for i in range(nbLig(image)):
        for j in range(nbCol(image)):
            L[i][j] = 255 - image[i][j]
    return L

def binaire(image, seuil):
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))]
    for i in range(nbLig(image)):
        for j in range(nbCol(image)):
            if image[i][j] < seuil :
                L[i][j] = 0
            else:
                L[i][j] = 1
    return L

print(nbLig(img))

print(nbCol(img))

print(negatif(img))

print(binaire(img,120))




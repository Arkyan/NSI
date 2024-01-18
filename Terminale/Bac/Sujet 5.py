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
assert paire_6([1, 2, 3, 4, 5]) == True

lancer2 = lancer(5)
print(paire_6(lancer2))
assert paire_6([1, 2, 3, 4, 6]) == True

lancer3 = lancer(3)
print(paire_6(lancer3))
assert paire_6([1, 6, 6]) == False

lancer4 = lancer(0)
print(paire_6(lancer4))
assert paire_6([]) == False



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

nbLig(img)
assert nbLig(img) == 4
nbCol(img)
assert nbCol(img) == 5
negatif(img)
assert negatif(img) == [[235, 221, 1, 110, 249], [232, 131, 18, 30, 186], [58, 81, 48, 230, 168], [0, 255, 231, 58, 66]]
binaire(img,120)
assert binaire(img,120) == [[0, 0, 1, 1, 0], [0, 1, 1, 1, 0], [1, 1, 1, 0, 0], [1, 0, 1, 1, 1]]



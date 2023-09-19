liste1 = [2*x for x in range(10)]
print("liste 1 [2*x for x in range(10)] est", liste1)

liste2 = [2*x+1 for x in range(10)]
print("liste 2 [2*x+1 for x in range(10)] est", liste2)

liste3 = [x**2 for x in range(10)]
print("liste 3 [2**2 for x in range(10)] est", liste3)

import math
liste4 = [math.sqrt(x) for x in liste3]
print("liste 4 [math.sqrt(x) for x in liste3] est", liste4)

l = [1,7,9,15,5,20,10,8]
liste5 = [p for p in l if p>10]
print("liste 5 [p for p in l if p>10] est", liste5)

liste6 = [p**2 for p in l if p <= 10]
print("liste 6 [p**2 for p in l if p <= 10] est", liste6)

#Afficher les différentes listes
def comprehens (liste7) :
    return [x**2 for x in liste7 if x>0],[x for x in liste7 if x>10]

liste8=[-4,-3,-2,0,1,5,9,11]
print(comprehens(liste8))

print("Le type de liste8 est :",type(comprehens(liste8)))
print("Le type du premier élément de liste8 est :",type(comprehens(liste8)[0]))
print("Le troisième élément du premier élément de liste8 est :",comprehens(liste8)[0][2])
print("Le type du troisième élément du premier élément de liste8 est : ", type(comprehens(liste8)[0][2]))
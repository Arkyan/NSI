L=[10,20,30]
print("La liste est : ",L)
print("La longueur de la liste :", len(L))
L.append(174)
L.append(5)
print("La liste à laquelle 174 et 5 sont ajoutés en fin de liste est : ",L)
print("La longueur de la liste est : ",L)
L.insert(1,32)
L.insert(4,183)
print("La liste à laquelle à 32 et 183 sont ajoutés en 2e et 5e position est : ",L)
print("La longeur de la liste est : ",len(L))
L.sort()
print("La liste ordonnée croissante est : ",L)
L.reverse()
print("La liste ordonnée décroissante est : ",L)
print("La cinquième valeur de la liste est : ",L[4])
L.pop()
print("La liste privée de sa dernière valeur est : ",L)
print("La longueur de la liste est : ",len(L))
L.pop(1)
print("La liste privée de sa deuxième valeur est : ",L)
L.pop(-3)
print("La liste privée de sa troisième valeur en partant de la fin est : ",L)
print("La longueur de la liste est : ",len(L))
L.extend([40,50,60])
print("La liste à laquelle 40,50,60 sont ajoutés en fin de liste est : ",L)
del L[2:6]
print("La liste privée des valeurs 3 à 5 est : ",L)
L.extend([80,90,100,110])
print("La liste à laquelle 80,90,100,110 sont ajoutés en fin de liste est : ",L)
L=L[1:6]
print("La liste dont on conserve de la 2e à la 6e valeurs est : ",L)


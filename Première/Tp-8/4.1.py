#Déclaration et remplissage d'une liste de 10 nombres
nombre = [2.16,3.43,9.22,2.32,4.23,4.26,0.97,6.58,7.69,1.89]
print(nombre)

#Trier la liste 
nombre.sort()
print("La liste triée est : ",nombre)

#Trouver l'index de l'élément 3.43 de la liste
print("L'indice de 3.43 est :",nombre.index(3.43))

#Inverser l'odre des éléments de la liste
nombre.reverse()
print("La liste inversée est :",nombre)

#Effacer l'élément 3.43 de la liste
nombre.remove(3.43)
print("La liste sans 3.43 est :",nombre)

#Effacer le 5ème élément de la liste 
nombre.remove(nombre[4])
print("La liste sans le 5ème élément est :",nombre)

#Insérer 6.33 en 3ème élément
nombre.insert(2,6.33)
print("La liste avec 6.33 inséré en 3ème élément de la liste est :", nombre)

#Ajouter l'élément 4.54 à la liste
nombre.append(4.54)
print("La liste à laquelle on ajoute 4.54 en dernier élément est :",nombre)

#Supprimer le 6ème élément de la liste
nombre.pop(5)
print("La liste à laquelle on a supprimer le 6ème élément est :",nombre)

#Supprimer le dernier élément de la liste 
nombre.pop()
print("La liste à laquelle on a supprimé le dernier élément est :",nombre)

#Effacer le 4ème élément de la liste 
del nombre[3]
print("La liste à laquelle on a supprimé le 4ème élément de la liste est :",nombre)

#Effacer du 2ème au 5ème élément de la liste
del nombre[1:4]
print("La liste à laquelle on a supprimé du 2ème au 5ème élément est :",nombre)

#Donner le type du deuxième élément
print("Le deuxième élément est de type", type(nombre[1]))

#Remplacer le deuxième élément par 2.36, les listes sont mutables
nombre[1] = 2.36
print("La liste dans laquelle on a remplacé le 2ème élément par 2.36 est :",nombre)

#Effacer la liste
nombre.clear()
print("La liste vide est :",nombre)

#Déclaration et remplissage d'un tuple vide
tuple1=()
print("Tuple vide : ", tuple1)

#Déclaration et remplissage d'un tuple avec un seul élément
#(La virgule n'est pas obligatoire mais fortement conseillée)
tuple2=(3,)
print("Tuple avec un seul élément :", tuple2)

#Déclaration et remplissage d'un tuple de 5 fois le même élément 
#Duplication
tuple3=(4.5,)*5
print("Tuple avec 5 fois le même élément : ",tuple3)

#Déclaration et remplissage d'un tuple avec 5 éléments
tuple4= (1,4,5,'moto', 4.6)
print("Tuple avec 5 éléments : ",tuple4)

#Déclaration et remplissage d'un tuple avec 5 éléments
#(Les paramètres ne sont pas obligatoires mais fortement consillés, à la lecture du code on sait directement que c'est un tuple)
tuple5 = 2,6,7,"vélo",6.8
print("Tuple avec 5 éléments déclarés sans paranthèses: ",tuple5)

#Obtenir le type de l'objet tuple5
print("Type de l'objet tuple5:",type(tuple5))

#Obtenir le type du 4ème élément du tuple5
print("Type du 4ème élément du tuple5 :",type(tuple5[3]))

#Obtenir le 4ème élément du tuple5
print("4ème élément du tuple5 :" ,tuple5[3])

#Obtenir le typle du 2ème élément du tuple5
print("Type du 2ème élément du tuple5 :",type(tuple5[1]))

#Obtenir le 2ème élément du tuple5
print("2ème élément du tuple5:",tuple5[1])

#Obtenir le type du dernier élément du tuple5 (indice négatif)
print("type du dernier élément du tuple 5 :",type(tuple5[-1]))

#Obtenir le dernier élément du tuple5 (idnice négatif)
print("Dernier élément du tuple5:", tuple5[-1])

#Obtenir le type  de l'avant dernier élément du tuple5 ('indice négatif)
print("Type de l'avant dernier élément du tuple5 :",type(tuple5[-2]))
print("tuple 5 : ", tuple5)

#Vérifier si l'élément ''vélo'' est dans le tuple 5
print("Vérifier si ''vélo'' est dans le tuple 5 : " , "vélo" in tuple5)

#Vérifier si l'élément ''5'' est dans le tuple 5
print("Vérifier si ''5'' est dans le tuple 5 : ", "5" in tuple5)

#Vérifier si l'élément 5 n'est pas dans le tuple 5
print("vérifier si ''5'' n'est pas dans le tuple 5 ", "5" not in tuple5)

#Donner la longueur du tuple
print("La longueur ou le nombre d'éléments du tuple 5 est : ", len(tuple5))

#Comparer 2 tuples
print("tuple4 : ", tuple4)
print("tuple5 : ", tuple5)
print("Les tuples 4 et 5 sont identiques : ", tuple4==tuple5)
tuple10 = tuple5
print("tuple10 : ", tuple10)
print("Les tuples 10 et 5 sont identiques :", tuple10 ==tuple5)

#Trouver l'indice d'un élément
print("L'indice de l'élément ''6'' du tuple 5 est : ", tuple5.index(6))
print("L'indice de l'élément ''vélo'' du tuple 5 est : ", tuple5.index("vélo"))

#Obtenir une partie du tuple5 (de l'indice 1 à 4 non compris)
print("Élément 1 à 4 non compris du tuple 5 : ",tuple5[1:4])

#Obtenir une partie du tuple 5 (de l'indice 0 à 4 non compris) par pas de 3 (une valeur de 3))
print("Élément 0 à 4 non compris par pas de 3 du tuple5 : ", tuple5[0:4:3])
print("tuple3 : ", tuple3)
print("tuple4 : ", tuple4)

#Concaténer 2 tuples pour en créer un autre
tuple6=tuple3 + tuple4
print("Concaténation tuple 3 et 4 : ", tuple6)
print("tuple5 : ", tuple5)

#Concaténer 2 fois le même tuple pour en créer un autre
tuple7 = tuple5*2
print("Concaténation 2 fois tuple 5 : ",tuple7)

#Nombre d'occurence dans un tuple
tuple11=tuple4+tuple3+tuple2+tuple3+tuple2
print("Concaténation des tuples 4,3,2,3,2 dans tuple 11 : ", tuple11)
print("Le nombre de 4,5 dans le tuple 11 est : ", tuple11.count(4.5))

#Disperser un tuple avec *
print("tuple 5 : ",tuple5)
print("tuple5 dispersé : ",*tuple5)

#Disperser l'élément d'un tuple
print("4ème élément du tuple5 : ", tuple5[3])
print("4ème élément dispersé du tuple5 : ", *tuple5[3])
print("2ème élément du 4ème élément du tuple5 : ",tuple5[3] [1])

#Utilisr la dispersion
tuple8=(14,4)
print("tuple8 : ", tuple8)
print("tuple5 : ", tuple5)
print("Somme des éléments du tuple 8 avec le 5ème éléments du tuple 5 : ", sum(tuple8,tuple5[4])) #faire la somme de tous les éléments d'un tuple et d'un autre nombre 

#La fonction divmod() prned deux nombres et donne leur quotient et reste de leur division entière sous forme d'une paire de nombres
#print(divmod(tuple8)) donne l'erreur :
#TypeError: divmod expected 2 arguments, got 1
#car il lui faut 2 arguments. Il faut donc disperser le tuple

print("Quotient et reste de la division entière des éléments du tuple 8 : ",divmod(*tuple8)) #fonctionne car tuple8 est dispersé en 2 arguments
print("tuple5 : ", tuple5)

#Concaténer 2 tuples + vs *
tuple9=(7,8,9)
print("tuple9 : ", tuple9)

#Concaténer 2 tuples avec +
print("Concaténation tuples 5 et 9 avec + : ",tuple5+tuple9)

#Concaténer 2 tuples avec *
print("Concaténation tuples 5 et 9 avec * : ", (*tuple5, *tuple9))

#On obtient la même chose 
#Les tuples sont immutables
print("Les tuples sont immutables : ",tuple5)

#tuple5[3]='vive le vélo !'
#En essayant de modifier le tuple on obtient l'erreur :
#TypeError: 'tuple' object does not supportitem assignment
#Les tuples sont itérables (on peut organiser une itération (boucle for) sur cette structure)
#Méthode 1
print("Méthode 1")
for element in tuple5 : #élément prend à chaque tour les éléments du tuple
    print("L'élément d'indice " , tuple5.index(element), "du tuple5 est : ",element)

#Méthode 2
print("Méthode 2")
for indice in range (len(tuple5)) : #parcourt des indices du tuple (len : donne la longueur du tuple)
    print("L'élément d'indice", indice, "du tuple 5 est :", tuple5[indice])
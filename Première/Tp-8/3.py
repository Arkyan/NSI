jours1 = ("lundi","mardi","mercredi","jeudi","vendredi")
jours2 = ("samedi","dimanche")

#Tester si samedi est un élément de jours1
print("Vérifier si ''samedi'' est dans jours1 : ", "samedi" in jours1)

#Donner la longueur de jours2
print("La longueur ou le nombre d'éléments de jours2 est : ", len(jours2))

#Tester si jours1 est égal à jours2
if jours1==jours2 : 
    print("Jours1 est égal à Jours2")
else :
    print("Jours1 n'est pas égal à Jours2")

#Donner le deuxième élément de jours1
print("Le deuxième élément de jours1 est :", jours1[1])

#Donner la partie de jours1 entre le deuxième élément compris et le quatrième élément compris par pas de 2 (une valeur sur 2)

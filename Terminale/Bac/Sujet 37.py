#Exo 1
def recherche(elt, tab):
    indice = -1
    for i in range(len(tab)):
        if elt == tab[i]:
            indice = i
    return indice

print("recherche(1, [2, 3, 4]) = ", recherche(1, [2, 3, 4]))
print("recherche(1, [10, 12, 1, 56]) = ", recherche(1, [10, 12, 1, 56]))
print("recherche(1, [1, 0, 42, 7]) = ", recherche(1, [1, 0, 42, 7]))
print("recherche(1, [1, 50, 1]) = " , recherche(1, [1, 50, 1]))
print("recherche(1, [8, 1, 10, 1, 7, 1, 8]) =", recherche(1, [8, 1, 10, 1, 7, 1, 8]))

assert recherche(1, [2, 3, 4]) == -1
assert recherche(1, [10, 12, 1, 56]) == 2
assert recherche(1, [1, 0, 42, 7]) == 0
assert recherche(1, [1, 50, 1]) == 2
assert recherche(1, [8, 1, 10, 1, 7, 1, 8]) == 5


print("--------------------")

#Exo 2
class AdresseIP:
    def __init__(self, adresse):
        self.adresse = adresse

    def liste_octet(self):
        return [int(i) for i in self.adresse.split(".")]

    def est_reservee(self):
        return self.liste_octet()[3] == 0 or self.liste_octet()[3] == 255

    def adresse_suivante(self):
        if self.liste_octet()[3] < 254:
            octet_nouveau = self.liste_octet()[3] + 1
            return AdresseIP('192.168.0.' + str(octet_nouveau))
        else:
            return False

adresse1 = AdresseIP('192.168.0.1')
adresse2 = AdresseIP('192.168.0.2')
adresse3 = AdresseIP('192.168.0.0')
 
print("Adresse 1 est réservée ? = ",adresse1.est_reservee())
print("Adresse 3 est réservée ? =",adresse3.est_reservee())
print(adresse2.adresse_suivante().adresse)

assert adresse1.est_reservee() == False
assert adresse3.est_reservee() == True
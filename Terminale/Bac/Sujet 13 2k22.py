#Exo 1
def rendu(somme_a_rendre):
    liste = [0,0,0]

    billets = [5,2,1]
    while somme_a_rendre > 0:
        index = 2
        if somme_a_rendre >= billets[0]:
            index = 0
        elif somme_a_rendre >= billets[1]:
            index = 1
        liste[index] += 1
        somme_a_rendre -= billets[index]

    return liste

print("rendu(3) =", rendu(3))
print("rendu(13) =", rendu(13))
print("rendu(64) =", rendu(64))
print("rendu(89) =", rendu(89))
assert rendu(-3) == [0,0,0]
assert rendu(13) == [2,1,1]
assert rendu(64) == [12,2,0]
assert rendu(89) == [17,2,0]

print("-----------------------------")

#Exo 2
class Maillon :
    def __init__(self,v) :
        self.valeur = v
        self.suivant = None

class File :
    def __init__(self) :
        self.dernier_file = None

    def enfile(self,element) :
        nouveau_maillon = Maillon(element)
        nouveau_maillon.suivant = self.dernier_file
        self.dernier_file = nouveau_maillon

    def est_vide(self) :
        return self.dernier_file == None

    def affiche(self) :
        maillon = self.dernier_file
        while maillon != None :
            print(maillon.valeur)
            maillon = maillon.suivant

    def defile(self) :
        if not self.est_vide() :
            if self.dernier_file.suivant == None :
                resultat = self.dernier_file.valeur
                self.dernier_file = None
                return resultat
            maillon = self.dernier_file
            while maillon.suivant.suivant != None :
                maillon = maillon.suivant
            resultat = maillon.suivant.valeur
            maillon.suivant = None
            return resultat
        return None

F = File()
print("F.est_vide() =", F.est_vide())
assert F.est_vide() == True
F.enfile(3)
print("F.affiche() =>")
F.affiche()

print("F.est_vide() =", F.est_vide())

F.enfile(5)
F.enfile(7)
assert F.est_vide() == False
print("F.affiche() =")
F.affiche()

print("F.defile() =", F.defile())
print("F.defile() =", F.defile())
print("F.affiche() =")
F.affiche()
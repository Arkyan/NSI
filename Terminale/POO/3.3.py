from random import randint

class Carte:
    def __init__(self, nom, couleur, valeur):
        all_cartes = ["2 de pique", "2 de coeur", "2 de carreau", "2 de trèfle", "3 de pique", "3 de coeur", "3 de carreau", "3 de trèfle", "4 de pique", "4 de coeur", "4 de carreau", "4 de trèfle", "5 de pique", "5 de coeur", "5 de carreau", "5 de trèfle", "6 de pique", "6 de coeur", "6 de carreau", "6 de trèfle", "7 de pique", "7 de coeur", "7 de carreau", "7 de trèfle", "8 de pique", "8 de coeur", "8 de carreau", "8 de trèfle", "9 de pique", "9 de coeur", "9 de carreau", "9 de trèfle", "10 de pique", "10 de coeur", "10 de carreau", "10 de trèfle", "valet de pique", "valet de coeur", "valet de carreau", "valet de trèfle", "dame de pique", "dame de coeur", "dame de carreau", "dame de trèfle", "roi de pique", "roi de coeur", "roi de carreau", "roi de trèfle", "as de pique", "as de coeur", "as de carreau", "as de trèfle"]
        
        for i in range(len(all_cartes)):
            if nom == all_cartes[i]:
                self.nom = nom
                self.valeur = valeur
                self.couleur = couleur
                return

        self.nom = nom
        self.couleur = couleur
        self.valeur = valeur
        
    def set_nom(self, nom, valeur) :
        self.nom = nom
        self.valeur = valeur
        
    def set_couleur(self, couleur) :
        self.couleur = couleur
        
    def get_nom(self) :
        return self.nom
    
    def get_couleur(self) :
        return self.couleur
    
    def get_valeur(self) :
        return self.valeur
    
    def est_egale_a(self, carte) :
        if self.valeur == carte.get_valeur() :
            return True
        else:
            return False
        
    def est_superieure_a(self, carte): 
        if self.valeur > carte.get_valeur():
            return True
        elif self.valeur == carte.get_valeur() and self.nom > carte.get_nom():
            return True
        elif self.valeur == carte.get_valeur() and self.nom == carte.get_nom() and self.couleur > carte.get_couleur():
            return True
        else:
            return False 
        
    def est_inferieure_a(self, carte):
        if self.valeur < carte.get_valeur():
            return True
        else:
            return False
    
    def __str__(self):
        return self.nom + " de " + self.couleur + " (" + str(self.valeur) + ")"

class Paquet : 
    def __init__(self):
        self.cartes = []

        # Ajouter les 52 cartes dans la liste 'cartes'
        for valeur in range(2, 15):
            for couleur in ["pique", "coeur", "carreau", "trèfle"]:
                nom = ""  # Définir le nom de la carte en fonction de la valeur
                if valeur == 11:
                    nom = "valet"
                elif valeur == 12:
                    nom = "dame"
                elif valeur == 13:
                    nom = "roi"
                elif valeur == 14:
                    nom = "as"
                else:
                    nom = str(valeur)

                carte = Carte(nom + " de " + couleur, couleur, valeur)
                self.cartes.append(carte)

    def battre(self):
        print("Le paquet a été battu")
        self.cartes.reverse()

    def ditribuer(self):
        print("La carte a été distribuée")
        carte_a_delete = self.cartes[0]
        del carte_a_delete
        return self.cartes[0]
    
    def __str__(self):
        for carte in self.cartes:
            print(carte)








c1 = Carte("as de trefle", "trèfle", 14)
c2 = Carte("roi de pique", "pique", 13)

c1.set_nom("as de pique", 10)
c1.set_couleur("coeur")

print(c1.est_superieure_a(c2))
print(c1.est_egale_a(c2))
print(c1.est_inferieure_a(c2))

Paquet().__str__()
print()
Paquet().battre()
Paquet().__str__()

print()
print("La taille du paquet de cartes est de", len(Paquet().cartes), "cartes")
print("Le type du paquet de cartes est", type(Paquet().cartes))
print("La première carte du paquet de cartes est : ", Paquet().cartes[0])
print("le nom de la première carte est : ", Paquet().cartes[0].get_nom())
print("la couleur de la première carte est : ", Paquet().cartes[0].get_couleur())
print("la valeur de la première carte est : ", Paquet().cartes[0].get_valeur())

print()
print("La carte distribuée est : ", Paquet().ditribuer())
print("La taille du paquet de cartes est de", len(Paquet().cartes), "cartes")

couleurs =('pique','coeur','carreau','trefle')
noms = ('2','3','4','5','6','7','8','9','10','valet','dame','roi','as')
valeurs = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6,"7": 7, "8": 8, "9": 9, "10": 10, "valet": 11,"dame": 12, "roi": 13, "as": 14}

 
class Carte:
    def __init__(self,couleur,nom,valeur):
        allcartes = []

        nom_carte = nom + " de " + couleur
        for couleur in couleurs:
            for nom in noms:
                allcartes.append(nom + " de " + couleur)

        for i in range(len(allcartes)) :
            if nom_carte == allcartes[i] :
                self.couleur = couleur
                self.nom = nom
                self.valeur = valeur
                break
            else :
                print("La carte",nom_carte,"n'existe pas")
                break
    def get_couleur(self) :
        return self.couleur
    def get_nom(self) :
        return self.nom
    def get_valeur(self) :
        return self.valeur
    def set_couleur(self, coul) :
        self.couleur = coul
        return self.couleur
    def set_nom(self, noom,valeeur) :
        self.nom = noom
        self.valeur = valeeur
carte1 = Carte("pique","2",2)
zbub
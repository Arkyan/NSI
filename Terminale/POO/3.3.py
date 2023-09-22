couleurs =('pique','coeur','carreau','trefle')
noms = ('2','3','4','5','6','7','8','9','10','valet','dame','roi','as')
valeurs = ['2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8':8, '9': 9, '10': 10, 'valet': 11, 'dame': 12, 'roi': 13, 'as': 14]

class Carte:
    def __init__(self,couleur,nom,valeur):
        self.couleur = couleur
        self.nom = nom
        self.valeur = valeur

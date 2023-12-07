from matplotlib import pyplot as plt

#4.4
class Arbre:
    def __init__(self):
        self._racine = None
        self._gauche = None
        self._droite = None
    def estVide(self):
        return self._racine is None
    def get_racine(self):
        assert not self.estVide(), "l'arbre est vide"
        return self._racine
    def get_sag(self):
        assert not self.estVide(), "l'arbre est vide"
        return self._gauche
    def get_sad(self):
        assert not self.estVide(), "l'arbre est vide"
        return self._droite

    def __str__(self):
        return "({},{},{})".format(self._gauche, self._racine, self._droite)
    def ecrire(self):
        if self.estVide():
            print("arbre vide")
        else:
            self._ecrire(0)
    def _ecrire(self, niveau):
        if self._droite:
            self._droite._ecrire(niveau + 1)
            print("{}{}".format(' ' * 4 * niveau, self._racine))
        if self._gauche:
            self._gauche._ecrire(niveau + 1)
    def ajouter(self, valeur):
        if self.estVide():
            self._racine = valeur
            self._gauche = Arbre()
            self._droite = Arbre()
        elif valeur < self._racine:
            self._gauche.ajouter(valeur)
        elif valeur > self._racine:
            self._droite.ajouter(valeur)
    

    def hauteur(self):
        if self.estVide():
            return 0
        else:
            return 1 + max(self._gauche.hauteur(), self._droite.hauteur())
        
    def _hauteur(self):
        if self.estVide():
            return 0
        else:
            return 1 + max(self._gauche._hauteur(), self._droite._hauteur())
        

    def _draw(self):
        # Méthode protégée permettant de tracer le graphique de l'ABR
        plt.rcParams.update({'font.size': 7})
        # Définition de la taille de police

            # Parcours en largeur
        an = []
        # Stockage des noeuds visités
        res = []
        # Stockage des noeuds parcourus en largeur
        posInit = 10 * self.hauteur()
        # Calculer la position des noeuds
        an.append((self, 0, posInit, "racine"))
        # Racine affichée en (0, posInit)
        # le parcours est terminé quand tous les noeuds ont été traités
        while (len(an) > 0):
            # Tant que les noeuds ne sont pas tous visités
            n = an[0]
            # Conserver le noeud courant pour gérer l'affichage
            res.append(n)
            # Ajouter le nouveau noeud visité à la liste res
            an.pop(0)
            # Retirer de la liste an des noeuds visités
            h = n[2] - 10
            # Calculer la position du noeud
            ecart = 20 * n[0].hauteur()**2
            # Améliorer l'affichage en écartant la position des noeuds

        # Les fils du noeud courant sont ajoutés
        # Tracer de l'arc / l'arête entre le noeud courant et les fils
        # gauche et droite
        if (n[0]._gauche is not None):
            # Si le sag n'est pas vide
            an.append((n[0]._gauche, n[1] - (ecart + h), h, "left"))
            # Ajouter le sag à la liste an
            plt.plot([n[1], n[1] - (ecart + h)], [n[2] - 3, h + 3],
            color='red', marker='o')
        # Tracer le sur le schéma
        if (n[0]._droite is not None):
            # Si le sad n'est pas vide
            an.append((n[0]._droite, n[1] + (ecart + h), h,"droite"))
            # Ajouter à la liste an
            plt.plot([n[1], n[1] + (ecart + h)], [n[2] - 3, h + 3], color='green', marker='o')

        # Tracer le sur le schéma
        # Une fois les noeuds positionnés, on les affiche, en calculant
        # la taille de graphique nécessaire
        xmin = res[0][1]
        # Mettre la première valeur dans x minimum
        xmax = res[0][1]
        # Mettre la première valeur dans x maximum
        # Calculer le décalage nécessaire pour que les noeuds ne se
        # chevauchent pas
        nbNoeuds = len(res)
        # Nombre de noeuds est égale à la longueur de la liste des
        # noeuds parcourus
        for x in res:
        # Pour tous les noeuds visités
            if (x[0] is not None):
        # S'il y a bien des noeuds dans l'ABR
                if (x[3] == "gauche"):
        # Faire un décalage adapté pour les fils gauche ou droite
                    decalage = (-nbNoeuds) * 2.5
        # Décaler de 2,5 * nombre de noeuds à gauche
            else:
        # Sinon
                decalage = nbNoeuds
        # Décaler de 1 * nombre de noeuds
                plt.annotate(str(x[0]._racine), (x[1] + decalage, x[2]))
        # La valeur du noeud est affichée
                if (x[1] < xmin):
        # Si la valeur à l'indice 1 est inférieur au minimum
                    xmin = x[1]
        # Modifier le minimum
                if (x[1] > xmax):
        # Si la valeur à l'indice 1 est supérieur au maximum
                    xmax = x[1]
        # Modifier le maximum
        plt.xlim(xmin - 100, xmax + 100)
        # Fixer la taille du schéma en largeur
        plt.ylim(-10, posInit + 10)
        # Fixer la taille du schéma en hauteur
        plt.show()
        # Afficher le schéma

    def parcoursPre(self) :
        if self.estVide():
            return []
        else:
            return [self._racine] + self._gauche.parcoursPre() + self._droite.parcoursPre()
            
    def parcoursLargeur(self):
        if self.estVide():
            return []
        else :
            return [self._racine] + self._gauche.parcoursLargeur() + self._droite.parcoursLargeur()
        
    def _parcoursLargeur(self):
        if self.estVide():
            return []
        else :
            return [self._racine] + self._gauche._parcoursLargeur() + self._droite._parcoursLargeur()
        

    def taille(self) :
        if self.estVide():
            return 0
        else:
            return 1 + self._gauche.taille() + self._droite.taille()
        
    def rechercher(self, valeur) :
        if self._racine is None :
            return False
        elif self._racine == valeur :
            return True
        else :
            if valeur < self._racine :
                return self._gauche.rechercher(valeur)
            else :
                return self._droite.rechercher(valeur)
            
    def minimum (self):
        Arbre = self 
        while Arbre._gauche is not None :
            Arbre = Arbre._gauche
        return Arbre._racine
    
    def maximum (self):
        Arbre = self 
        while Arbre._droite is not None :
            Arbre = Arbre._droite
        return Arbre._racine
        
    

def listeToArbre(Lst):
    for i in Lst:
        arb.ajouter(i)
        print(arb)
    arb.ecrire()
    arb._draw()

arb = Arbre()
Liste = [13,26,18,5,3,4,12,18,6,7]
listeToArbre(Liste)


print("La hauteur de l'arbre binaire de recherche est : ",arb.hauteur()) 
print("Le parcours en largeur de l'arbre binair de recherche est :",arb.parcoursLargeur())
print("La taille de l'arbre binaire de recherche est : ",arb.taille())

            
for val in range(0, 30) :
    print("La clé", val, "est dans l'arbre binaire de recherche", arb.rechercher(val))
    
print("Le maximum de l'arbre binaire de recherche est : ",arb.maximum())
print("Le minimum de l'arbre binaire de recherche est : ",arb.minimum())

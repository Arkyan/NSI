import matplotlib.pyplot as plt 
#3.3
class Arbre: # Arbre binaire en POO
    def __init__(self,valeur):
        self._racine = valeur
        self._gauche = None
        self._droite = None
    def set_gauche(self, sousarbre):
        self._gauche = sousarbre
    def set_droite(self, sousarbre):
        self._droite = sousarbre
    def get_gauche(self):
        return self._gauche
    def get_droite(self):
        return self._droite 
    def get_racine(self):
        return self._racine
    def __str__(self):
        return "({},{},{})".format(self._gauche, self._racine,self._droite)

arbr = Arbre(4)
print(arbr)
arbr.set_gauche(Arbre(3))
print(arbr)
arbr.set_droite(Arbre(1))
print(arbr)
arbr.get_droite().set_gauche(Arbre(2))
print(arbr)
arbr.get_droite().set_droite(Arbre(7))
print(arbr)
arbr.get_gauche().set_gauche(Arbre(6))
print(arbr)
arbr.get_droite().get_droite().set_gauche(Arbre(9))
print(arbr)

print("La racine du sag du sad de l'arbre est : ", arbr.get_droite().get_gauche().get_racine())
print("La racine du sag du sad de l'arbre est : ", arbr.get_gauche().get_gauche().get_racine()) 
print("La racine du sag du sad de l'arbre est : ", arbr.get_droite().get_droite().get_gauche().get_racine()) 

#3.3.1.1
from queue import Queue
def BFS(arbre):
    file = Queue()
    file.put(arbre)
    resultat = []
    while file.empty() is False :
        element = file.get()
    if element is not None :
        print("L'arbre ou le sous arbre est : ",element)
    resultat.append(element.get_racine())
    print(resultat)
    file.put(element.get_gauche())
    file.put(element.get_droite())
    return resultat

print("---------- C'est la BFS (Breadth First Search), parcours en largeur d’abord ----------")
print("Le parcours en largeur d’abord de l'arbre donne la liste suivante : ",BFS(arbr)) 

#3.3.1.2.1
def prefixe(arbre):
    resultat = []
    resultat.append(arbre._racine)
    if arbre._gauche is not None:
        resultat.append(prefixe(arbre._gauche))
    if arbre._droite is not None:
        resultat.append(prefixe(arbre._droite))
    return resultat

def aplatirListe(liste):
    for element in liste:
        if type(element) == list:
            aplatirListe(element)
        else:
            listePlate.append(element)
        return listePlate

print("---------- C'est la DFS (Depth First Search), parcours préfixe en profondeur d’abord ----------")

print("Le parcours préfixe en profondeur de l'arbre donne la liste suivante : ",prefixe(arbr)) 
listePlate = [] 
print("Le parcours préfixe en profondeur de l'arbre donne la liste aplatie suivante : ",aplatirListe(prefixe(arbr)))

def infixe(arbre):
    resultat = []
    if arbre._gauche is not None:
        resultat.append(infixe(arbre._gauche))
    resultat.append(arbre._racine)
    if arbre._droite is not None:
        resultat.append(infixe(arbre._droite))
    return resultat


#3.3.2
def taille(arbre) :
    if arbre is None :
        return 0
    else :
        return 1 + taille(arbre._gauche) + taille(arbre._droite)
    
#3.3.3
def hauteur(arbre) :
    if arbre is None :
        return 0
    else :
        return 1 + max(hauteur(arbre._gauche), hauteur(arbre._droite))
   
#3.3.4  
def recherche(arbre, valeur) :
    if arbre is None :
        return False
    elif arbre._racine == valeur :
        return True
    else :
        return recherche(arbre._gauche, valeur) or recherche(arbre._droite, valeur)
print("------ Recherche d'une clé (valeur) dans l'arbre ------")
for val in range(0,21):
    print("La clé",val,"est dans l'arbre : ",recherche(arbr,val)) 

#4.1
def aplatirListe(liste,listeplateparcoursinfixe) :
    for element in liste :
        if type(element) == list :
            aplatirListe(element,listeplateparcoursinfixe)
        else :
            listeplateparcoursinfixe.append(element)
    return listeplateparcoursinfixe

def est_abr(arbre,list) :
    listeplateparcoursinfixe = []
    listeplateparcoursinfixe = aplatirListe(infixe(arbre),listeplateparcoursinfixe)
    return listeplateparcoursinfixe == list


# ARBRE BINAIRE N°1 mais pas un arbre binaire de recherche
print("----- Arbre N°1 pas ABR -----")
arbr = Arbre(4)
# Instancier / Créer l'arbre dont le nœud a pour valeur 4, les sag
# et sad sont None
print(arbr) # Afficher l'arbre
arbr.set_gauche(Arbre(3))
# Instancier / Créer l'arbre dont le nœud a pour valeur 3, les sag
# et sad sont None pour sag de a
print(arbr) # Afficher l'arbre
arbr.set_droite(Arbre(1))
# Instancier / Créer l'arbre dont le nœud a pour valeur 1, les sag
# et sad sont None pour sad de a
print(arbr) # Afficher l'arbre
arbr.get_droite().set_gauche(Arbre(2))
# Instancier / Créer l'arbre dont le nœud a pour valeur 2, les sag
# et sad sont None pour sag du sad de a
print(arbr) # Afficher l'arbre
arbr.get_droite().set_droite(Arbre(7))
# Instancier / Créer l'arbre dont le nœud a pour valeur 7, les sag
# et sad sont None pour sad du sad de a
print(arbr) # Afficher l'arbre
arbr.get_gauche().set_gauche(Arbre(6))
# Instancier / Créer l'arbre dont le nœud a pour valeur 6, les sag
# et sad sont None pour sag du sag de a
print(arbr) # Afficher l'arbre
arbr.get_droite().get_droite().set_gauche(Arbre(9))
# Instancier / Créer l'arbre dont le nœud a pour valeur 9, les sag
# et sad sont None pour sag du sag du sad de a
print(arbr) # Afficher l'arbre
# ARBRE BINAIRE N°2 et un arbre binaire de recherche
print("\n----- Arbre N°2 ABR -----")
arbr2 = Arbre(5)
# Instancier / Créer l'arbre dont le nœud a pour valeur 4, les sag
# et sad sont None
print(arbr2) # Afficher l'arbre
arbr2.set_gauche(Arbre(2))
# Instancier / Créer l'arbre dont le nœud a pour valeur 3, les sag
# et sad sont None pour sag de a
print(arbr2) # Afficher l'arbre
arbr2.set_droite(Arbre(7))
# Instancier / Créer l'arbre dont le nœud a pour valeur 1, les sag
# et sad sont None pour sad de a
print(arbr2) # Afficher l'arbre
arbr2.get_droite().set_gauche(Arbre(6)) 
# Instancier / Créer l'arbre dont le nœud a pour valeur 2, les sag
# et sad sont None pour sag du sad de a
print(arbr2) # Afficher l'arbre
arbr2.get_droite().set_droite(Arbre(8))
# Instancier / Créer l'arbre dont le nœud a pour valeur 7, les sag
# et sad sont None pour sad du sad de a
print(arbr2) # Afficher l'arbre
arbr2.get_gauche().set_gauche(Arbre(0))
# Instancier / Créer l'arbre dont le nœud a pour valeur 6, les sag
# et sad sont None pour sag du sag de a
print(arbr2) # Afficher l'arbre
arbr2.get_gauche().set_droite(Arbre(3))
# Instancier / Créer l'arbre dont le nœud a pour valeur 6, les sag
# et sad sont None pour sag du sag de a
print(arbr2) # Afficher l'arbre
print("\n---------- Test ABR ----------")
print("\n--- Test arbre binaire N°1 pas ABR ---")
print("Le parcours infixe en profondeur de l'arbre N°1 donne la liste suivante : ",infixe(arbr))
# Créer une liste de liste contenant le parcours infixe
print("Le parcours infixe en profondeur de l'arbre N°1 donne la liste aplatie suivante : ",aplatirListe(infixe(arbr),[]))
# Créer une liste aplatie contenant le parcours infixe
print("L'arbre binaire N°1 est un arbre binaire de recherche : ", est_abr(arbr, aplatirListe(infixe(arbr),[])))
# Vérifier si l'arbre est une ABR en vérifiant si la liste aplatie
# est ordonnée
print("\n--- Test arbre binaire N°2 ABR ---")
print("Le parcours infixe en profondeur de l'arbre N°1 donne la liste suivante : ",infixe(arbr2))
print("Le parcours infixe en profondeur de l'arbre N°2 donne la liste aplatie suivante : ",aplatirListe(infixe(arbr2),[]))
print("L'arbre binaire N°2 est un arbre binaire de recherche : ", est_abr(arbr2, aplatirListe(infixe(arbr2),[]))) 

#4.2
def rechercheabr(arbre, valeur) :
    if arbre is None :
        return False
    elif arbre._racine == valeur :
        return True
    elif arbre._racine > valeur :
        return rechercheabr(arbre._gauche, valeur)
    else :
        return rechercheabr(arbre._droite, valeur)
    
print("\n--- Test ABR ---")
print("Le parcours infixe en profondeur de l'arbre N°1 donne la liste suivante : ",infixe(arbr2))
print("Le parcours infixe en profondeur de l'arbre N°2 donne la liste aplatie suivante : ",aplatirListe(infixe(arbr2),[]))
print("L'arbre binaire N°2 est un arbre binaire de recherche : ", est_abr(arbr2, aplatirListe(infixe(arbr2),[])))
print("\n---------- Recherche d'une clé (valeur) dans l'arbre binaire de recherche ----------")
for val in range(0,21):
    print("La clé",val,"est dans l'arbre binaire de recherche : ",rechercheabr(arbr2,val))

#4.3
def insertion(arbre, valeur) :
    if arbre is None :
        return Arbre(valeur)
    elif arbre._racine > valeur :
        arbre.set_gauche(insertion(arbre._gauche, valeur))
    else :
        arbre.set_droite(insertion(arbre._droite, valeur))
    return arbre

print("\n---------- Insérer une clé (valeur) dans l'arbre binaire de recherche ----------")
vale = 1
vale1 = 4
vale2 = 14
vale3 = 8
print("Insertion de la clé",vale,"dans l'arbre binaire de recherche N°2 : ", insertion(arbr2, vale))
print("Insertion de la clé",vale1,"dans l'arbre binaire de recherche N°2 : ", insertion(arbr2, vale1))
print("Insertion de la clé",vale2,"dans l'arbre binaire de recherche N°2 : ", insertion(arbr2, vale2))
print("Insertion de la clé",vale3,"dans l'arbre binaire de recherche N°2 : ", insertion(arbr2, vale3))
print("\n--- Test ABR ---")
print("Le parcours infixe en profondeur de l'arbre N°1 donne la liste suivante : ",infixe(arbr2))
print("Le parcours infixe en profondeur de l'arbre N°2 donne la liste aplatie suivante : ",aplatirListe(infixe(arbr2),[]))
print("L'arbre binaire N°2 est un arbre binaire de recherche : ", est_abr(arbr2, aplatirListe(infixe(arbr2),[])))
print("\n---------- Recherche d'une clé (valeur) dans l'arbre binaire de recherche ----------")
for val in range(0,21):
    print("La clé",val,"est dans l'arbre binaire de recherche : ",rechercheabr(arbr2,val)) 

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

def listeToArbre(Lst):
    for i in Lst:
        arb.ajouter(i)
        print(arb)
    arb.ecrire()
    arb._draw()

arb = Arbre()
Liste = [13,26,18,5,3,4,12,18,6,7]
listeToArbre(Liste)

def hauteur(self):
    if self.estVide():
        return 0
    else:
        return 1 + max(self._gauche.hauteur(), self._droite.hauteur())

def hauteur(self):
    if self.estVide():
        return 0
    else:
        return 1 + max(self._gauche._hauteur(), self._droite._hauteur())

print("La hauteur de l'arbre binaire de recherche est : ",arb.hauteur()) 

def draw(self):
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
        
#Exo 1 
def nombre_de_mots(phrase):
    nb = 0
    id_der = len(phrase)-1
    for c in phrase:
        if c == " ":
            nb = nb + 1
    if phrase[id_der] == "?" or phrase[id_der] == "!":
        return nb
    else :
        return nb+1

print('nombre_de_mots("Cet exercice est simple.") =', nombre_de_mots("Cet exercice est simple."))
print('nombre_de_mots("Le point d exclamation est separe !") =', nombre_de_mots("Le point d exclamation est separe !"))
print('nombre_de_mots("Combien de mots y a t il dans cette phrase ?") =', nombre_de_mots("Combien de mots y a t il dans cette phrase ?"))
print('nombre_de_mots("Fin.") =', nombre_de_mots("Fin."))

assert nombre_de_mots("Cet exercice est simple.") == 4
assert nombre_de_mots("Le point d exclamation est separe !") == 6
assert nombre_de_mots("Combien de mots y a t il dans cette phrase ?") == 10
assert nombre_de_mots("Fin.") == 1


print('-------------------')

#Exo 2
class Noeud:
    def __init__(self, valeur):
        self.valeur = valeur
        self.gauche = None
        self.droit = None
    def getValeur(self):
        return self.valeur
    def droitExiste(self):
        return (self.droit is not None)
    def gaucheExiste(self):
        return (self.gauche is not None)
    def inserer(self, cle):
        if cle < self.valeur :
            if self.gaucheExiste():
                self.gauche.inserer(cle)
            else:
                self.gauche = Noeud(cle)
        elif cle > self.valeur:
            if self.droitExiste():
                self.droit.inserer(cle)
            else:
                self.droit  = Noeud(cle)

arbre = Noeud(7)
for cle in (3, 9, 1, 6):
    arbre.inserer(cle)
    
print("arbre.gauche.getValeur() =", arbre.gauche.getValeur())
print("arbre.droit.getValeur() =", arbre.droit.getValeur())
print("arbre.gauche.gauche.getValeur() =", arbre.gauche.gauche.getValeur())
print("arbre.gauche.droit.getValeur() =", arbre.gauche.droit.getValeur())

assert arbre.gauche.getValeur() == 3
assert arbre.droit.getValeur() == 9
assert arbre.gauche.gauche.getValeur() == 1
assert arbre.gauche.droit.getValeur() == 6
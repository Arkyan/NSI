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
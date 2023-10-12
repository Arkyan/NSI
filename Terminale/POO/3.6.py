list = ["+", "*", "-", "/", 10, 2, 4, 3, 6]

class Pile() :
    def __init__(self, pile):
        self.pile = pile

    def empiler(self, element):
        self.pile.append(element)

    def vide(self):
        return len(self.pile) == 0
    
    def depiler(self):
        if len(self.pile) == 0:
            print("Attention votre pile est vide donc on ne peut pas dépiler")
            return None
        else :
            return self.pile.pop()
        
    def taille(self):
        return len(self.pile)
    
    def sommet(self):
        if self.vide():
            return "Attention votre pile est vide donc elle est sans sommet"
        else :
            return self.pile[0]
        
    def __str__(self):
        pile = ""
        for i in range(len(self.pile)):
            pile += "|   " + str(self.pile[i]) + "   |" + "\n"  

        return "Etat de la pile : " + "\n" + pile
    
class Maillon() :
    def __init__(self, valeur, suivant):
        self.valeur = valeur
        self.suivant = suivant
        
    def set_valeur(self, valeur, suivant):
        self.valeur = valeur
        if suivant == None:
            self.suivant = None
        else :
            self.suivant = suivant

def prefixe(liste) :
    pile = Pile([])
    for i in range(len(liste)-1, -1, -1):
        if liste[i] in ["+", "-", "*", "/"]:
            a = pile.depiler()
            b = pile.depiler()
            pile.empiler(str(liste[i]) + " " + str(a) + " " + str(b))
        else :
            pile.empiler(liste[i])
    return pile.depiler()

pile = Pile([])
print(prefixe(list))
pile.empiler(6)
print(pile)
pile.empiler(3)
print(pile)
pile.empiler(4)
print(pile)
pile.empiler(2)
print(pile)
pile.empiler(10)
print(pile)
pile.depiler()
print(pile)
pile.depiler()
print(pile)
pile.empiler(5.0)
print(pile)
pile.depiler()
pile.depiler()
pile.empiler(1.0)
print(pile)
pile.depiler()
pile.depiler()
pile.depiler()
pile.empiler(9.0)
print(pile)
print("Le résultat de l'expression préfixée (" + str(prefixe(list)) + ") est : " + str(pile.depiler()))

pile.empiler(3)
print(pile)

pile.empiler(2)
print(pile)

pile.depiler()
pile.depiler() 
pile.empiler(6)
print(pile)

pile.empiler(1)
print(pile)

pile.depiler()
pile.depiler()
pile.empiler(7)
print(pile)

print("Le résultat de l'expression préfixée (" + str(prefixe(list)) + ") est : " + str(pile.depiler()))

pile.depiler()
pile.empiler(3)
print(pile)

pile.empiler(2)
print(pile)

pile.empiler(1)
print(pile)

pile.depiler()
pile.depiler()
pile.empiler(3)
print(pile)

pile.depiler()
pile.depiler()
pile.empiler(9)

print("Le résultat de l'expression préfixée (" + str(prefixe(list)) + ") est : " + str(pile.depiler()))
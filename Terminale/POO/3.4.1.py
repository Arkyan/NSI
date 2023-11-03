class Pile :
    def __init__(self) :
        self.pile = []

    def empiler(self, element) :
        self.pile.append(element)

    def vide(self) :
        return self.pile == []
    
    def depiler(self) :
        if self.vide() :
            return print("La pile est vide donc vous ne pouvez pas dépiler !")
        else :
            return self.pile.pop()
        
    def taille (self) :
        return len(self.pile)
    
    def sommet(self) :
        if self.vide() :
            return print("La pile est vide donc pas de sommet !")
        else :
            return self.pile[-1]
        
    def __str__(self):
        pile = ""
        for i in range(len(self.pile)):
            pile += "|   " + str(self.pile[i]) + "   |" + "\n"  

        return "Etat de la pile : " + "\n" + pile
class Maillon : 
    def __init__(self, valeur, suivant) :
        self.valeur = valeur
        self.suivant = suivant

    def set_valeur(self, valeur, suivant):
        self.valeur = valeur
        if suivant == None:
            self.suivant = None
        else :
            self.suivant = suivant


pile = Pile()
print("La pile est vide : ", pile.vide())
print("Le sommet de la pile est : ", pile.sommet())
print("La taille de la pile est : ", pile.taille())
print("On dépile : ", pile.depiler())
print("On empile 2 : ", pile.empiler(2))
print(str(pile))
print("La pile est vide : ", pile.vide())
print("On empile 5 : ", pile.empiler(5))
print(str(pile))
print("Le sommet de la pile est : ", pile.sommet())
print("La taille de la pile est : ", pile.taille())
print("On empile 7 : ", pile.empiler(7))
print(str(pile))
print("Le sommet de la pile est : ", pile.sommet())
print("La taille de la pile est : ", pile.taille())
print("On dépile", pile.depiler())
print(str(pile))
print("On dépile", pile.depiler())
print(str(pile))
print("Le sommet de la pile est : ", pile.sommet())
print("La taille de la pile est : ", pile.taille())
print("On dépile", pile.depiler())
print(str(pile))
print("On dépile encore !!!")        
print(pile.depiler())
print(str(pile))






        
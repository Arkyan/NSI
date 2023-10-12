class Pile:
    def __init__(self, le_sommet=None):
        self.le_sommet = le_sommet

    def set_sommet(self, le_sommet):
        self.le_sommet = le_sommet

    def vide(self):
        return self.le_sommet == None

    def empiler(self, element):  # le sommet de la pile devient un maillon
        self.le_sommet = Maillon(element, self.le_sommet)

    # Une méthode dépiler permettant de dépiler le premier élément de la pile (Le sommet suivant de la pile devient le sommet)
    def depiler(self):
        if self.le_sommet is None:
            return None

        sommet_actuel = self.le_sommet
        self.le_sommet = sommet_actuel.sommet_suivant
        return sommet_actuel.element

    def __str__(self):
        stack_representation = []
        sommet_actuel = self.le_sommet

        while sommet_actuel is not None:
            stack_representation.append(str(sommet_actuel.element))
            sommet_actuel = sommet_actuel.sommet_suivant

        return '|' + '|'.join(stack_representation) + '|'


class Maillon:
    def __init__(self, contenu, suivant):
        self.element = contenu
        self.sommet_suivant = suivant

    def set_contenu(self, contenu):
        self.element = contenu

    def set_suivant(self, suivant):
        self.sommet_suivant = suivant


class File:
    def __init__(self, entree, sortie):
        self.entree = entree
        self.sortie = sortie

    def set_entree(self, entree):
        self.entree = Pile(entree)

    def set_sortie(self, sortie):
        self.sortie = Pile(sortie)

    def vide(self):
        return self.entree.vide() and self.sortie.vide()

    def enfiler(self, element):
        self.entree.empiler(element)

    def defiler(self):
        if self.vide():
            print("On défile une file vide")
            return None

        if self.sortie.vide():
            while not self.entree.vide():
                element = self.entree.depiler()
                self.sortie.empiler(element)
        return self.sortie.depiler()

    def __str__(self):
        return "Entree : " + str(self.entree) + "\nSortie : " + str(self.sortie)

    
pile = Pile()
pile2 = Pile()
file = File(pile, pile2)
print(pile)
print("On enfile 5")
pile.empiler(5)
print(file)

print("On enfile 8")
pile.empiler(8)
print(file)
 
print("On enfile 11")
pile.empiler(11)
print(file)

print("On defile")
file.defiler()
print(file)

print("On enfile 3")
pile.empiler(3)
print(file)

print("On enfile 7")
pile.empiler(7)
print(file)

print("On defile")
file.defiler()
print(file)

print("On defile")
file.defiler()
print(file)

print("On defile")
file.defiler()
print(file)

print("On defile")
file.defiler()
print(file)

file.defiler()
    
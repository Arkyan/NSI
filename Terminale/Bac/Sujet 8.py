Exercice N°1
"""

print("\033[92mExercice N°1\033[0m")

def max_dico(tableau) :
    maxi_num = 0
    maxi_label = ""
    for label, num in tableau.items() :
        if num > maxi_num :
            maxi_num  = num
            maxi_label = label

    return (maxi_label, maxi_num)


print(max_dico({'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50}))
assert max_dico({'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50}) == ('Ada', 201)
print(max_dico({'Alan': 222, 'Ada': 201, 'Eve': 220, 'Tim': 50}))
assert max_dico({'Alan': 222, 'Ada': 201, 'Eve': 220, 'Tim': 50}) == ('Alan', 222)
print()

"""
Exercice N°2
"""

print("\033[92mExercice N°2\033[0m")

class Pile:
    """
    Classe definissant une structure de pile.
    """
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        """
        Renvoie le booleen True si la pile est vide, False sinon.
        """
        return self.contenu == []

    def empiler(self, v):
        """
        Place l'element v au sommet de la pile
        """
        self.contenu.append(v)

    def depiler(self):
        """
        Retire et renvoie l'element place au sommet de la pile,
        si la pile n'est pas vide.
        """
        if not self.est_vide():
            return self.contenu.pop()


def eval_expression(tab):
    p = Pile()
    for element in tab:
        if element != '+' and element != '*':
            p.empiler(element)
        else:
            if element == '+':
                resultat = p.depiler() + p.depiler()
            else:
                resultat = p.depiler() * p.depiler()
            p.empiler(resultat)
    return p.depiler()

print(eval_expression([2, 3, '+', 5, '*']))

assert eval_expression([2, 3, '+', 5, '*']) == 25
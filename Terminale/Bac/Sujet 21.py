#Exo 1
def delta(liste):
    tab = [liste[0]]
    for i in range(1, len(liste)):
        tab.append(liste[i]-liste[i-1])
    return tab

print("delta([1000, 800, 802, 1000, 1003]) =", delta([1000, 800, 802, 1000, 1003]))
print("delta([42]) =", delta([42]))

assert delta([1000, 800, 802, 1000, 1003]) == [1000, -200, 2, 198, 3]
assert delta([42]) == [42]

#Exo 2
class Noeud:
    def __init__(self, g, v, d):
        self.gauche = g
        self.valeur = v
        self.droit = d

    def __str__(self):
        return str(self.valeur)

    def est_une_feuille(self):
        return self.gauche is None and self.droit is None


def expression_infixe(e):
    s = ''
    if e.gauche is not None:
        s = '(' + s + expression_infixe(e.gauche) + ')'
    s = s + str(e.valeur)
    if e.droit is not None:
        s = s + '(' + expression_infixe(e.droit) + ')'
    return s


e = Noeud(Noeud(Noeud(None, 3, None),
    '*', Noeud(Noeud(None, 8, None), '+', Noeud(None, 7, None))),
    '-', Noeud(Noeud(None, 2, None), '+', Noeud(None, 1, None)))
print("expression_infixe(e) =", expression_infixe(e))
assert expression_infixe(e) == "((3)*((8)+(7)))-((2)+(1))"
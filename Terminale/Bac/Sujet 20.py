#Exo 1
def ajoute_dictionnaires(d1, d2):
    d = d1
    for k, v in d2.items():
        if k in d:
            d[k] += v
        else:
            d[k]  = v
    return d

print('ajoute_dictionnaires({1: 5, 2: 7}, {2: 9, 3: 11}) =' , ajoute_dictionnaires({1: 5, 2: 7}, {2: 9, 3: 11}))
print('ajoute_dictionnaires({}, {2: 9, 3: 11}) =' , ajoute_dictionnaires({}, {2: 9, 3: 11}))
print('ajoute_dictionnaires({1: 5, 2: 7}, {}) =' , ajoute_dictionnaires({1: 5, 2: 7}, {}))

assert ajoute_dictionnaires({1: 5, 2: 7}, {2: 9, 3: 11}) == {1: 5, 2: 16, 3: 11}
assert ajoute_dictionnaires({}, {2: 9, 3: 11}) == {2: 9, 3: 11}
assert ajoute_dictionnaires({1: 5, 2: 7}, {}) == {1: 5, 2: 7}

print('-------------------')

#Exo 2
from random import randint

def nbre_coups():
    n = 0
    cases_vues = [0]
    case_en_cours = 0
    nbre_cases = 12
    while len(cases_vues) < 12:
        x = randint(1, 6)
        case_en_cours = (case_en_cours + x) % 12
        if case_en_cours not in cases_vues:
            cases_vues.append(case_en_cours)
        n = n + 1
    return n

print('nbre_coups() =', nbre_coups())

assert nbre_coups() >= 12
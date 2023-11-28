#Exo 1
def liste_puissances(a, n):
    tab = [a]
    for _ in range(2, n+1):
        r = tab[-1]*a
        tab.append(r)
    return tab

def liste_puissances_borne(a, borne):
    if borne <= a:
        return []
    tab = [a]
    c = True
    while c:
        r = tab[-1]*a
        if r < borne:
            tab.append(r)
        else :
            c = False
    return tab

print(liste_puissances(3, 5))
print(liste_puissances(-2, 4))
print(liste_puissances_borne(2, 16))
print(liste_puissances_borne(2, 17))
print(liste_puissances_borne(5, 5))
assert liste_puissances(3, 5) == [3, 9, 27, 81, 243]    
assert liste_puissances(-2, 4) == [-2, 4, -8, 16]
assert liste_puissances_borne(2, 16) == [2, 4, 8]
assert liste_puissances_borne(2, 17) == [2, 4, 8, 16]
assert liste_puissances_borne(5, 5) == []
            
print("------------------------------------------------")   
#Exo 2
dico = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6,
        "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
        "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17,
        "R": 18, "S": 19, "T": 20, "U": 21, "V": 22,
        "W": 23, "X": 24, "Y": 25, "Z": 26}


def est_parfait(mot):
    code_concatene = ""
    code_additionne = 0
    for c in mot:
        code_concatene = code_concatene + str(dico[c])
        code_additionne = code_additionne + dico[c]
    code_concatene = int(code_concatene)
    if code_concatene % code_additionne == 0 :
        mot_est_parfait = True
    else:
        mot_est_parfait = False
    return code_additionne, code_concatene, mot_est_parfait

print(est_parfait("PAUL"))
print(est_parfait("ALAIN"))
assert est_parfait("PAUL") == (50, 1612112, False) 
assert est_parfait("ALAIN") == (37, 1121914, True)

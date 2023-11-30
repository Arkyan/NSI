#Exo 1
def correspond(mot, mot_a_trous):
    n1 = len(mot)
    n2 = len(mot_a_trous)
    if n1 != n2:
        return False
    for i in range(n1):
        if mot[i] != mot_a_trous[i] and mot_a_trous[i] != '*':
            return False
    return True

print(correspond('INFORMATIQUE', 'INFO*MA*IQUE'))
print(correspond('AUTOMATIQUE', 'INFO*MA*IQUE'))
print(correspond('STOP', 'S*'))
print(correspond('AUTO', '*UT*'))
assert correspond('INFORMATIQUE', 'INFO*MA*IQUE') == True
assert correspond('AUTOMATIQUE', 'INFO*MA*IQUE') == False
assert correspond('STOP', 'S*') == False 
assert correspond('AUTO', '*UT*') == True


print("---------------------------------")


#Exo 2
def est_cyclique(plan):
    expediteur = 'A'
    destinataire = plan[expediteur]
    nb_destinaires = 1 
    
    while destinataire != expediteur:
        destinataire = plan[destinataire]
        nb_destinaires += 1

    return nb_destinaires == len(plan)

print(est_cyclique({'A':'E', 'F':'A', 'C':'D', 'E':'B', 'B':'F','D':'C'}))
print(est_cyclique({'A':'E', 'F':'C', 'C':'D', 'E':'B', 'B':'F','D':'A'}))
print(est_cyclique({'A':'B', 'F':'C', 'C':'D', 'E':'A', 'B':'F','D':'E'}))
print(est_cyclique({'A':'B', 'F':'A', 'C':'D', 'E':'C', 'B':'F','D':'E'}))
assert est_cyclique({'A':'E', 'F':'A', 'C':'D', 'E':'B', 'B':'F','D':'C'}) == False
assert est_cyclique({'A':'E', 'F':'C', 'C':'D', 'E':'B', 'B':'F','D':'A'}) == True
assert est_cyclique({'A':'B', 'F':'C', 'C':'D', 'E':'A', 'B':'F','D':'E'}) == True 
assert est_cyclique({'A':'B', 'F':'A', 'C':'D', 'E':'C', 'B':'F','D':'E'}) == False
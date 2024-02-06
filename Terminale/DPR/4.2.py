def tri_fusion(liste):
    if len(liste) <= 1:
        return liste
    else:
        milieu = len(liste) // 2
        gauche = tri_fusion(liste[:milieu])
        droite = tri_fusion(liste[milieu:])
        return fusion(gauche, droite)

def fusion(partieA, partieB):
    if len(partieA) == 0:
        return partieB
    elif len(partieB) == 0:
        return partieA
    elif partieA[0] < partieB[0]:
        return [partieA[0]] + fusion(partieA[1:], partieB)
    else:
        return [partieB[0]] + fusion(partieA, partieB[1:])
    
list1 = [35, 13, 4, 22, 7, 17, 3]
list2 = [39, 28, 44, 4, 10, 80, 11]
list3 = [22, 11, 3, 55, 37, 30, 44, 59, 2]
list4 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print ("La liste", list1, "triée par tri fusion est : ", tri_fusion(list1))
print ("La liste", list2, "triée par tri fusion est : ", tri_fusion(list2))
print ("La liste", list3, "triée par tri fusion est : ", tri_fusion(list3))
print ("La liste", list4, "triée par tri fusion est : ", tri_fusion(list4)) 

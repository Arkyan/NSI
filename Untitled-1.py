resultats = {'Dupont': {
                           'DS1': [15.5, 4],
                           'DM1': [14.5, 1],
                           'DS2': [13, 4],
                           'PROJET1': [16, 3],
                           'DS3': [14, 4]
                       },
             'Durand': {
                           'DS1': [6 , 4],
                           'DM1': [14.5, 1],
                           'DS2': [8, 4],
                           'PROJET1': [9, 3],
                           'IE1': [7, 2],
                           'DS3': [8, 4],
                           'DS4':[15, 4]
                       }
            }

def moyenne(nom,dico_result) :
    if nom in dico_result :
        notes = dico_result[nom]
        totalpoints = 0
        totalcoeff = 0
        for valeurs in notes.values() :
            note, coeff = valeurs
            totalpoints = totalpoints + note * coeff
            totalcoeff = totalcoeff + coeff
        return round(totalpoints / totalcoeff,1)
    











def recherche_indices_classement(elt,tab) :
    liste1 = []
    liste2 = []
    liste3 = []
    for i in range(len(tab)) :
        if tab[i] > elt :
            liste1.append(i)
        elif tab[i] < elt :
            liste2.append(i)
        else :
            liste3.append(i)
    return liste2,liste3,liste1

print(recherche_indices_classement(3,[1,3,4,2,4,6,3,0]))
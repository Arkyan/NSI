"""
Exercice N°1
"""

print("\033[92mExercice N°1\033[0m")

def rangement_valeurs(notes_eval):
    valeurs_final = []
    for i in range(11):
        total = 0
        for note in notes_eval:
            if i == note:
                total += 1
        valeurs_final.append(total)
    return valeurs_final

def notes_triees(effectifs):
    notes_final = []
    for i in range(len(effectifs)):
        for j in range(effectifs[i]):
            notes_final.append(i)
    return notes_final

notes_eval = [2, 0, 5, 9, 6, 9, 10, 5, 7, 9, 9, 5, 0, 9, 6, 5, 4]

print("rangement_valeurs(notes_eval) ->", rangement_valeurs(notes_eval))
print("notes_triees(rangement_valeurs(notes_eval)) ->", notes_triees(rangement_valeurs(notes_eval)))

assert rangement_valeurs(notes_eval) == [2, 0, 1, 0, 1, 4, 2, 1, 0, 5, 1]
assert notes_triees(rangement_valeurs(notes_eval)) == [0, 0, 2, 4, 5, 5, 5, 5, 6, 6, 7, 9, 9, 9, 9, 9, 10]

print()

"""
Exercice N°2
"""

print("\033[92mExercice N°2\033[0m")

def dec_to_bin (nb_dec):
    q, r = nb_dec // 2, nb_dec % 2
    if q == 0:
        return str(r)
    else:
        return dec_to_bin(q) + str(r)

def bin_to_dec(nb_bin):
    if nb_bin == '0':
        return 0
    elif nb_bin == '1':
        return 1
    else:
        if nb_bin[-1] == '0':
            bit_droit = 0
        else:
            bit_droit = 1
        return 2 * bin_to_dec(nb_bin[:-1]) + bit_droit

print("dec_to_bin(25) ->", dec_to_bin(25))

assert dec_to_bin(25) == "11001"

print("bin_to_dec('101010') ->", bin_to_dec('101010'))

assert bin_to_dec('101010') == 42
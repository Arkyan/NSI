def binaire(nbre) :
    if nbre == 0 :
        return [0]
    elif nbre > 0 :
        return binaire(nbre // 2) + [nbre % 2]
    
nbre = int(input("Veuillez saisir un nombre entier puis validez avec <<Enter>> : "))
print("La liste est : ", binaire(nbre))
en_binaire = str(binaire(nbre)).replace("[", "").replace("]", "").replace(",", "").replace(" ", "")
print("Le nombre décimal", nbre, "donne", en_binaire, "en binaire.") 


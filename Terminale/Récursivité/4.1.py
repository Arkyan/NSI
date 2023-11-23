def occurence (lettre, mot) :
    if mot == "" :
        return 0
    elif mot[0] == lettre :
        return 1 + occurence (lettre, mot[1:])
    else :
        return occurence (lettre, mot[1:])
    
lettre = input("Entrez une lettre : ")
mot = input("Entrez un mot : ")

resultat = occurence(lettre, mot)

print("Dans la phrase" , mot , "il y a" , resultat , "fois la lettre" , lettre)
def renverse(chaine) :
    if len(chaine) <= 1 :
        return chaine
    else :
        return chaine[-1] + renverse(chaine[0:len(chaine) - 1])
    
chaine = int(input("Entrez une chaine de caractères : "))
print("La chaine de caractères",chaine,"renversée est", renverse(chaine))


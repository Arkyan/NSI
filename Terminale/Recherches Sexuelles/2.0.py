def recherche_textuelle_naive(motif, texte):
    reponse = []
    t = len(texte)
    m = len(motif)
    for i in range(0, t - m + 1):
        if texte[i : i + m] == motif:
            reponse.append(i)
    return reponse
print(recherche_textuelle_naive("TAGGAC", "TAGTAGCACTGTAGGACTGC"))
print(recherche_textuelle_naive("TAGGAC", "TAGTAGCACTGTAAGGACTGC"))
print(recherche_textuelle_naive("TAGGAC", "TAGTAGCACTGTAGGACTGCTAGGACCCA"))
print(recherche_textuelle_naive("TAGGAC", "TAGTAGCACTGTAGGACTGCTAGGACCCATAGTAGCACTGTAGGACTGC"))
print(recherche_textuelle_naive("maison", "une magnifique maison bleue"))
print(recherche_textuelle_naive("ma","une magnifique maison bleue"))
print(recherche_textuelle_naive("u","une magnifique maison bleue"))
print(recherche_textuelle_naive("u","Une magnifique maison bleue"))
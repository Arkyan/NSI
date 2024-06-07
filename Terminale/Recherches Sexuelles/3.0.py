def table_boyer_moore(motif):
    d = [{} for i in range(len(motif))]
    for j in range(len(motif)):
        for k in range(j):
            d[j][motif[k]] = k
    return d

def decalage(d, j, chr):
    if chr in d[j]:
        return j - d[j][chr]
    else:
        return j + 1
    
def recherche_boyer_moore(motif, texte):
    d = table_boyer_moore(motif)
    i = 0
    reponse = []
    while i < len(texte) - len(motif):
        k = 0
        for j in range(len(motif)-1, -1, -1):
            if texte[i + j] != motif[j]:
                k = decalage(d, j, texte[i + j])
        if k == 0: 
            reponse.append(i)
            k = 1
        i = i + k
    return reponse
print(recherche_boyer_moore("TAGGAC", "TAGTAGCACTGTAGGACTGC"))
print(recherche_boyer_moore("TAGGAC", "TAGTAGCACTGTAAGGACTGC"))
print(recherche_boyer_moore("TAGGAC", "TAGTAGCACTGTAGGACTGCTAGGACCCA"))
print(recherche_boyer_moore("TAGGAC", "TAGTAGCACTGTAGGACTGCTAGGACCCATAGTAGCACTGTAGGACTGC"))
print(recherche_boyer_moore("maison","une magnifique maison bleue"))
print(recherche_boyer_moore("ma","une magnifique maison bleue"))
print(recherche_boyer_moore("u","une magnifique maison bleue"))
print(recherche_boyer_moore("u","Une magnifique maison bleue")) 
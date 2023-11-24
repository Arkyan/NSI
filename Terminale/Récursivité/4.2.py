def inserer_element_dans_liste_triee(elem,lst) :
    if lst == [] :
        return [elem]
    elif elem < lst[0] :
        return [elem] + lst
    else :
        return [lst[0]] + inserer_element_dans_liste_triee(elem,lst[1:])
    
def tri_insertion(lst) :
    if lst == [] :
        return []
    else :
        return inserer_element_dans_liste_triee(lst[0],tri_insertion(lst[1:]))

liste = eval(input("Entrez une liste : "))
resultat = tri_insertion(liste)
print("La liste triée est : ",resultat)

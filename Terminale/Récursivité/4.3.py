def min_list(lst) :
    if lst == [] :
        return None
    elif len(lst) == 1 :
        return lst[0]
    else :
        m = min_list(lst[1:])
        if m < lst[0] :
            return m
        else :
            return lst[0]
        
def tri_selection(lst) :
    if lst == [] :
        return []
    else :
        m = min_list(lst)
        return [m] + tri_selection([x for x in lst if x != m])

liste = eval(input("Entrez une liste : "))
resultat = tri_selection(liste)
print("La liste triée est : ",resultat)

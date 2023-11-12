def compteARebours(nbre):
    if nbre <= 0 :
        return 
    elif nbre > 0 :
        print(nbre)
        return compteARebours(nbre - 1)
    
compteARebours(5) 

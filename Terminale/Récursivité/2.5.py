def som_n_prem_entiers(nbre) :
    if nbre == 0 :
        return 
    elif nbre > 0 :
        return nbre + som_n_prem_entiers(nbre - 1)
    
print("La somme des 100 premiers entiers naturels est : ", som_n_prem_entiers(100))

        
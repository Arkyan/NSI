def puissance_recursive_DPR(nbre,puis) :
    if puis >= 0 :
        if puis == 0 :
            return 1
        else :
            return nbre * puissance_recursive_DPR(nbre,puis-1)
        

print("Ce programme permet de calculer, récursivement en utilisant la méthode <<Diviser pour régner>>, la puissance d'un nombre sans utiliser l'opérateur d'exponentiation (**)")
nbre = input("Veuillez saisir le nombre : ")
puis = input("Veuillez saisir la puissance : ")

print("La puissance de ",nbre," à la puissance ",puis," est : ",puissance_recursive_DPR(int(nbre),int(puis)))



    

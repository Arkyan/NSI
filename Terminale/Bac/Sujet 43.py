#Exo 1
def ecriture_binaire_entier_positif(n):
    tab = [n%2]
    n = n // 2
    while n > 0:
        tab.append(n%2)
        n = n // 2
    tab.reverse()
    return tab
        
#Exo 2
def tri_bulles(T):
    n = len(T)
    for i in range(len(T)-1,0,-1):
        for j in range(i):
            if T[j] > T[j+1]:
                temp = T[j]
                T[j] = T[j+1]
                T[j+1] = temp
    return T
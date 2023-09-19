def tableMultTuple(nbre) : 
    return (1*nbre , 2*nbre , 3*nbre , 4*nbre , 5*nbre , 6*nbre , 7*nbre , 8*nbre , 9*nbre)

tableDe = 0
tableDe = int(input("Je veux la table de :"))
tuple = tableMultTuple(tableDe)
print("Le tuple est ", tuple)
print(type(tableMultTuple(tableDe)))
print("Voici la table de multiplication de", tableDe, ":")
for i in range (1,10) :
    print(tableDe,"*",i, "=", tableMultTuple(tableDe), ":")
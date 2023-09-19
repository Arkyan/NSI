def tableMult(nbre) : 
    for i in range (1,11) : 
        print(nbre,"*", i,"=",i*nbre)
    #return None

tableDe = int(input("Je veux la table de :"))
print("Voici la table de pultiplication de", tableDe, ":")
tableMult(tableDe)
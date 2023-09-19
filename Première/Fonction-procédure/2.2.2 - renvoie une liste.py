def tableMultList(nbre) : 
    global listeMult
    listeMult = [nbre * x for x in range(1,10)]
    return listeMult
listeMult = []
tableDe = int(input("Je veux la table de :"))
print("La lsite est",tableMultList(tableDe))
print(type(tableMultList(tableDe)))
print("Voci la table de multiplication de", tableDe, ":")
for i in range (1,10) : 
    print(tableDe,"*", i, "=", listeMult[i-1])


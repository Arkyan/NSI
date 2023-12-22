#Exo 1
def fusion(tab1, tab2):
    n1 =  len(tab1)
    n2 = len(tab2)
    i1 = 0
    i2  = 0
    tab=[]
    while i1 < n1 and i2 < n2:
        if tab1[i1] > tab2[i2]:
            tab.append(tab2[i2])
            i2 = i2 + 1
        else :
            tab.append(tab1[i1])
            i1 = i1 + 1
    while i1 < n1 :
        tab.append(tab1[i1])
        i1 = i1 + 1
    while i2 < n2 :
        tab.append(tab2[i2])
        i2 = i2 + 1
    return tab

print(fusion([3, 5], [2, 5]))
print(fusion([-2, 4], [-3, 5, 10]))
print(fusion([4], [2, 6]))
assert fusion([3, 5], [2, 5]) == [2, 3, 5, 5]
assert fusion([-2, 4], [-3, 5, 10]) == [-3, -2, 4, 5, 10]
assert fusion([4], [2, 6]) == [2, 4, 6]

print("---------------------")

#Exo 2
romains = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

def traduire_romain(nombre) :
    if len(nombre) == 1:
        return romains[nombre[0]]

    elif romains[nombre[0]] >= romains[nombre[1]] :
        return romains[nombre[0]] + traduire_romain(nombre[1:])
    else:
        return  traduire_romain(nombre[1:]) - romains[nombre[0]]

print(traduire_romain("XIV"))
print(traduire_romain("CXLII"))
print(traduire_romain("MMXXIII"))
assert traduire_romain("XIV") == 14
assert traduire_romain("CXLII") == 142
assert traduire_romain("MMXXIII") == 2023


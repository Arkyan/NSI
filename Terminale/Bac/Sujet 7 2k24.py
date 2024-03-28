#Exo 1
def gb_vers_entier(tab):
    s = 0
    n = len(tab)
    for i in range(n):
        v = tab[n - 1 - i]
        if v :
            s = s + 2**i
    return s

tab = [True, False, True, False, False, True, True]
print(gb_vers_entier([]))
print(gb_vers_entier([True]))
print(gb_vers_entier([True, False, True,False, False, True, True]))
print(gb_vers_entier([True, False, False, False,False, False, True, False]))    
assert gb_vers_entier([]) == 0
assert gb_vers_entier([True]) == 1
assert gb_vers_entier([True, False, True,False, False, True, True]) == 83
assert gb_vers_entier([True, False, False, False,False, False, True, False]) == 130

print('----------------------')

#Exo 2
def tri_insertion(tab):
    n = len(tab)
    for i in range(1, n):
        valeur_insertion = tab[i] 
        j = i 
        while j > 0 and valeur_insertion < tab[j-1]: 
            tab[j] = tab[j-1]
            j = j - 1 
        tab[j] = valeur_insertion 

tab = [98, 12, 104, 23, 131, 9]
tri_insertion(tab)
print(tab)
assert tab == [9, 12, 23, 98, 104, 131]
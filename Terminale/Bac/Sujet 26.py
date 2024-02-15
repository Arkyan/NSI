#Exo 1
def multiplication(n1, n2) :
    s=0
    if n1==0 or n2==0:
        return 0
    if n1<0:
        return -multiplication(-n1,n2)
    if n2<0:
        return -multiplication(n1,-n2)
    for i in range(n2):
        s = s+n1
    return s

print("multiplication(3, 5) =", multiplication(3, 5))
print("multiplication(-4, -8) =",multiplication(-4, -8))
print("multiplication(-2, 6) =",multiplication(-2, 6))
print("multiplication(-2, 0) =",multiplication(-2, 0))

assert multiplication(3, 5) == 15
assert multiplication(-4, -8) == 32
assert multiplication(-2, 6) == -12
assert multiplication(-2, 0) == 0

print("--------------------")

#Exo 2
def dichotomie(tab, x):
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut + fin) // 2
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
             fin = m - 1
    return False

print("dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 28) =", dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 28))
print("dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 27) =", dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 27))

assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 28) == True
assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 27) == False
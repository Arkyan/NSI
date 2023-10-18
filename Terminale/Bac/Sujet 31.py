#Exo 1 
def nb_repetitions(elt, tab):
    c = 0
    for v in tab:
        if v == elt:
            c = c + 1
    return c

print(nb_repetitions(5, [2, 5, 3, 5, 6, 9, 5]))
assert nb_repetitions(5, [2, 5, 3, 5, 6, 9, 5]) == 3

print(nb_repetitions('A', [ 'B', 'A', 'B', 'A', 'R']))
assert nb_repetitions('A', [ 'B', 'A', 'B', 'A', 'R']) == 2

print(nb_repetitions(12, [1, '! ', 7, 21, 36, 44]))
assert nb_repetitions(12, [1, '! ', 7, 21, 36, 44]) == 0

#Exo 2
def binaire(a):
    bin_a = str(a%2)
    a = a // 2
    while a > 0 :
        bin_a = str(a%2) + bin_a
        a = a // 2
    return bin_a

print(binaire(0))
assert binaire(0) == '0'

print(binaire(77))
assert binaire(77) == '1001101'
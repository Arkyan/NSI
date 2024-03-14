#Exo 1 
def moyenne (tab):
    s = 0
    for v in tab:
        s = s + v
    return s / len(tab)

print("moyenne([1.0]) ->", moyenne([1.0]))
print("moyenne([1.0, 2.0, 4.0]) ->", moyenne([1.0, 2.0, 4.0]))

assert moyenne([1.0]) == 1.0
assert moyenne([1.0, 2.0, 4.0]) == 7 / 3


#Exo 2
def binaire(a):
    bin_a = str(a % 2)
    a = a // 2
    while a > 0 :
        bin_a = str(a % 2) + bin_a
        a = a // 2
    return bin_a


print("binaire(83) ->", binaire(83))
print("binaire(127) ->", binaire(127))
print("binaire(0) ->", binaire(0))

assert binaire(83) == "1010011"
assert binaire(127) == "1111111"
assert binaire(0) == "0"

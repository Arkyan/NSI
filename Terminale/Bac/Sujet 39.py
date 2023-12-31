#Exo 1 
def fibonacci(n):
    suite = [0] * (n+1)
    for i in range(1, n+1):
        if i < 3:
            suite[i] = 1
        else:
            suite[i] = suite[i-1] + suite[i-2]
    return suite[n]

print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(25))
print(fibonacci(45))
assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(25) == 75025
assert fibonacci(45) == 1134903170

#Exo 2
def pantheon(eleves, notes):
    note_maxi = 0
    meilleurs_eleves =  []

    for i in range(len(eleves)) :
        if notes[i] == note_maxi :
            meilleurs_eleves.append(eleves[i])
        elif notes[i] > note_maxi:
            note_maxi = notes[i]
            meilleurs_eleves = [eleves[i]]

    return (note_maxi,meilleurs_eleves)



eleves_nsi = ['a','b','c','d','e','f','g','h','i','j']
notes_nsi = [30, 40, 80, 60, 58, 80, 75, 80, 60, 24]

print(pantheon(eleves_nsi, notes_nsi)) 
assert pantheon(eleves_nsi, notes_nsi) == (80, ['c', 'f', 'h'])
print(pantheon([],[])) 
assert pantheon([],[]) == (0, [])
    
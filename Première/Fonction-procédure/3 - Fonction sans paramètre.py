from random import *

def tirerDé() :
    return randint(1, 6)

for i in range (10) :
    faceDé = tirerDé()

print("Tirage du dé n°", i+1, ":", faceDé)
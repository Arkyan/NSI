from math import *

masse = int(input('Entrez votre masse en kg :'))
taille = float(input('Entrez votre taille en m :'))

imc = masse/(taille*taille)
imc = round(imc, 1)
print(str(imc))
if imc < 16.5 :
    print("Il y a beaucoup trop d'écart avec une corpulence normale")
elif imc >= 16.5 and imc < 18.5 :
    print("Il y a un léger écart avec une corpulence normale ")
elif imc >= 18.5 and imc < 25 :
    print("Vous avez une corpulence normale")
elif imc >= 25 and imc < 30 :
    print("Il y a un écart léger avec une corpulence normale")
elif imc >= 30 and imc < 35 :
    print("Il y a beaucoup trop d'écart avec une corpulence normale")
else :
    print("Il y a une obésité sévère, morbide ou massive")

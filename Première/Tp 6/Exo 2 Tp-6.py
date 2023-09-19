from math import * 
magnitude = float(input( 'Veuillez saisir la magnitude du séisme :' ))
amplitudeMax = round(10**(magnitude-5.8), 3)
print('La magnitude que vous avez saisi est de :'+ str(magnitude))
print("L\'amplitude max est de :" + str(amplitudeMax))
if magnitude < 5 :
    print ('Le séisme ne crée pas de dégats')
elif magnitude >=5 and magnitude < 5.5 :
    print ('Le séisme crée quelques dégâts')
elif magnitude >=5 and magnitude < 6.5 :
    print ('Le séisme crée des dégâts importants')
elif magnitude >=5 and magnitude < 7.5 :
    print ('Le séisme crée un désastre important')
else :
    print ('Le séisme crée une catastrophe')
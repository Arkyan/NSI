Km = float(input("Saisir le nombre de kilomètres à parcourir : "))
Jour = float(input("Saisir le nombre de jour de location : "))

coutdiesel = ( 38*Jour + 9*Km )
coutessence = ( 30*Jour + 15*Km )
print("La voiture diesel vous coûtera : " + str(coutdiesel) + " €" )
print("La voiture essence vous coûtera : " + str(coutessence) + " €")

if coutdiesel > coutessence :
    print("La voiture essence est plus appropriée")
else :
    print ("La voiture diesel est plus appropiée")

     
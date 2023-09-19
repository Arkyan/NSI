vitesseVehicule = int(input("Saississez la vitesse du véhicule en km/h :"))


def reaction (réaction) :
    vréaction = réaction/3.6
    vréaction = round(vréaction,2)
    return vréaction

def freinageSec (vitesse_Fs) :
    lFs = vitesse_Fs**2/200
    lFs = round(lFs,2)
    return lFs

def freinageMouille (vitesse_Fm) :
    lFm = vitesse_Fm**2/100
    lFm = round(lFm,2)
    return lFm

def arrêtSec (vitesse_as) :
    lAs = freinageSec(vitesse_as) + reaction(vitesse_as)    
    lAs = round(lAs,2)
    return lAs

def arrêtmouillé (vitesse_am) :
    lAm = freinageMouille(vitesse_am) + reaction(vitesse_am)
    lAm = round(lAm,2)
    return lAm
 
 

print("- Sur route sèche : \n    * Une distance de réaction est de " + str(reaction(vitesseVehicule)), "\n    * Une distance de de freinage est de " + str(freinageSec(vitesseVehicule)), "\n    * Soit une distance d'arrêt de " + str(arrêtSec(vitesseVehicule)), "\n       Roulez doucement sur route sèche", "\n- Sur route mouillé :", "\n    * Une distance de réaction de " + str(reaction(vitesseVehicule)), "\n    * Une distance de freinage de " + str(freinageMouille(vitesseVehicule)), "\n    * Soit une distance d'arrêt de " + str(arrêtmouillé(vitesseVehicule)), "\n         ROULEZ TRÈS LENTEMENT SUR ROUTE MOUILLÉE")   
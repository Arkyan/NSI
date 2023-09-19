from tkinter import * 
from math import *

Total = 0

for NumMois in range (1,13) :
    if NumMois == 1 :
        mois = "Janvier"
    elif NumMois == 2 :
        mois = "Février"
    elif NumMois == 3 :
        mois = "Mars"
    elif NumMois == 4 :
        mois = "Avril"
    elif NumMois == 5 :
        mois = "Mai"
    elif NumMois == 6 :
        mois = "Juin"
    elif NumMois == 7 :
        mois = "Juillet"
    elif NumMois == 8 :
        mois = "Août"
    elif NumMois == 9 :
        mois = "Septembre"
    elif NumMois == 10 :
        mois = "Octobre"
    elif NumMois == 11 :
        mois = "Novembre"
    elif NumMois == 12 :
        mois = "Décembre"
    Salaire = float(input( "Saisissez le salaire du mois de " + mois + " : "))
    Total = Total + Salaire
    Total = round(Total,2) 

print("Votre salaire annuel est de " + str(Total) + " €. ")
                    

class CompteBancaire :
    solde = 0
    def __init__(self,nom,solde) :
        self.nom = nom
        self.solde = solde

    def get_nom(self) :
        return self.nom
    def get_solde(self) :
        return self.solde
    def __str__(self) : 
        return f"{self.nom,self.solde}"
    def set_solde(self, sold) :
        self.solde = sold
        return self.solde
    def depot(self,sold) :
        self.solde += sold
        return self.solde
    def retrait(self,sold) :
        self.solde -= sold
        if self.solde<sold :
            print("ATTENTION votre solde est insuffisant pour pouvoir faire ce retrait")
        else :
            return self.solde
    def affichage(self) :
        print("Le compte bancaire appartient à :", self.get_nom())
        print("Le solde est de :", self.get_solde(),"$")
    def set_nom(self, nomm) :
        self.nom = nomm
        return self.nom
    def piratage(self) :
        Compte2547.set_nom("Jules")
        return 


Compte2547 = CompteBancaire("Bob",300.1)
Compte2547.affichage()
Compte2547.piratage() 
Compte2547.affichage()

     

    

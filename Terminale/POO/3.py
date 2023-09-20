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
        self._solde = sold
        return self._solde
    

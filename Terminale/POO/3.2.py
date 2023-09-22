class Table :
    def __init__(self, ref,matière,masse,longueur,largeur,hauteur,prixvente,prixfab,stock) :
        self.ref = ref
        self.matière = matière
        self.masse = masse
        self.longueur = longueur
        self.largeur = largeur
        self.hauteur = hauteur
        self.prixvente = prixvente
        self.prixfab = prixfab
        self.stock = stock 
    def get_ref(self) : 
        return self.ref
    def get_matiere(self) : 
        return self.matière
    def get_masse(self) : 
        return self.masse
    def get_longueur(self) : 
        return self.longueur
    


        
        
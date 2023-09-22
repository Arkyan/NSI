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
    def get_largeur(self) : 
        return self.largeur
    def get_hauteur(self) :
        return self.hauteur
    def get_prixvente(self) :
        return self.prixvente
    def get_prixfab(self) :
        return self.prixfab
    def get_stock(self) :
        return self.stock
    
    def set_ref(self, reff) : 
        self.ref = reff
        return self.ref
    def set_matiere(self, matt) : 
        self.matière = matt
        return self.matière
    def set_masse(self, mass) : 
        self.masse = mass
        return self.masse
    def set_longueur(self, longg) : 
        self.longueur = longg
        return self.longueur
    def set_largeur(self, largg) : 
        self.largeur = largg
        return self.largeur
    def set_hauteur(self, hautt) :
        self.hauteur = hautt
        return self.hauteur
    def set_prixvente(self,prixv) :
        self.prixvente = prixv
        return self.prixvente
    def set_prixfab(self,prixf) :
        self.prixfab = prixf
        return self.prixfab
    def set_stock(self, stook) :
        self.stock = stook
        return self.stock
    def AFFICHAGE(self) :
        print("")
    


        
        
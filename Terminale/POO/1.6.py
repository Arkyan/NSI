class Personnes :
    def __init__(self,prenom,genre,age) :
        self.prenom = prenom
        self.genre = genre 
        self.age = age
        
alex = Personnes("Alex","masculin",15)
bob = Personnes("Bob","masculin",20)
beatrice = Personnes("Béatrice","féminin",14)
elsa = Personnes("Elsa","féminin",17)

print(alex)
print("Le prénom d'Alex est",alex.prenom)
print("Le genre d'Alex est",alex.genre)
print("L'âge d'Alex est",alex.age)

print(bob)
print("Le prénom de Bob est",bob.prenom)
print("Le genre de Bob est",bob.genre)
print("L'âge de Bob est",bob.age)

print(beatrice)
print("Le prénom de Béatrice est",beatrice.prenom)
print("Le genre de Béatrice est",beatrice.genre)
print("L'âge de Béatrice est",beatrice.age)

print(elsa)
print("Le prénom d'Elsa est",elsa.prenom)
print("Le genre d'Elsa est",elsa.genre)
print("L'âge d'Elsa est",elsa.age)

def __repr__(self) : 
    return f"{self.prenom,self.genre,self.age}"

def __str__(self) : 
    return f"{self.prenom,self.genre,self.age}"

def get_age(self) :
    print("Récupération de l'age de la personne")
    return self.age

print("Modification avec getter et setter")
print("")
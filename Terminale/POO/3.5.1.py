class File :
    def __init__(self, file):
        self.file = file

    def enfiler(self, element):
        self.file.append(element)
    
    def vide(self):
        return self.file == []
    
    def defiler(self):
        if self.vide():
            return print("La file est vide donc vous ne pouvez pas défiler !")
        else :
            return self.file.pop(0)
    
    def taille(self):
        return len(self.file)
    
    def sommet(self):
        if self.vide():
            return print("La file est vide donc pas de sommet !")
        else :
            return self.file[0]
        
    def __str__(self):
        file = ""
        for i in range(len(self.file)):
            file += "|   " + str(self.file[i]) + "   |" + "\n"  
        return "Etat de la file : " + "\n" + file
    
file = File([])
print("La file est vide : ", file.vide())
print("Le sommet de la file est : ", file.sommet())
print("La taille de la file est : ", file.taille())
print("On défile : ", file.defiler())
print("Défiler")
print(file)
print("On enfile 2")
file.enfiler(2) 
print(file)

print("La file est vide : ", file.vide())
print("On enfile 5")
file.enfiler(5)
print(file)

print("Le sommet de la file est : ", file.sommet())
print("La taille de la file est : ", file.taille())
print("On enfile 7")
file.enfiler(7)
print(file)

print("Le sommet de la file est : ", file.sommet())
print("La taille de la file est : ", file.taille())

print("On défile 2")
file.defiler()
print(file)

print("On défile 5")
file.defiler()
print(file)

print("Le sommet de la file est : ", file.sommet())
print("La taille de la file est : ", file.taille())

print("On défile 7")
file.defiler()
print(file)

print("On défile encore !!!", file.defiler())
print(file)
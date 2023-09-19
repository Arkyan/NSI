class Mangling : 
    def __init__(self, variable=50) : 
        self._maVar = variable/5
        self.__maVar = variable
        self.maVar = variable*3

    def get_var(self) :
        return self.__maVar*2
objet = Mangling()
print(dir(objet))
print(objet)
print(objet.maVar)
print(objet._maVar)
print(objet.get_var())
print(objet._Mangling__maVar)
#print(objet.__maVAr)
objet1 = Mangling(40)
print(dir(objet1))
print(objet1)
print(objet1.maVar)
print(objet1._maVar)
print(objet1.get_var()) 
print(objet1._Mangling__maVar)
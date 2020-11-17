# PYTHON OO 17/11/2020 17:00 Part-1
class Animal:
    def __init__(self,a,b):
        self.name=a
        self.species=b

class Cat(Animal):
    def __init__(self,name,spe,owner):
        self.owner = owner
        Animal.__init__(self,a,b)

a = Animal("Rex","Dog")
b = Cat("Tom","Persian","James")
print(a.name, a.species)
print(b.name,b.species,b.owner)
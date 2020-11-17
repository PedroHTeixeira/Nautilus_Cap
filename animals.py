# PYTHON OO 17/11/2020 17:00 Part-1
class Animal:
    def __init__(self,a,b):
        self.name=a
        self.species=b
    def __repr__(self):
        return f"This animal is a {self.species}, which is named {self.name}"

class Cat(Animal):
    def __init__(self,name,spe,owner):
        self.owner = owner
        Animal.__init__(self,name,spe)

a = Animal("Rex","Dog")
b = Cat("Tom","Persian","James")

print(a)
print(b)
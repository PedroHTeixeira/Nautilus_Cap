class Animal:
    def __init__(self,a,b):
        self.nome=a
        self.especie=b

a = Animal("Rex","Cachorro")
print(a.nome, a.especie)
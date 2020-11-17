# PYTHON OO 17/11/2020 17:00 Part-2

class City:
    def __init__(self,name,pop):
        self.population = pop
        self.name=name

    def __repr__(self): 
        r = "The city {} have {} people".format(self.name,self.population)
        return r
    
    def __add__(self, other): # Sum
        if type(other) == int:
            return self.population + other
        else:
            return self.population + other.population

    def __gt__(self,other):#Greater Than
        return self.population > other.population

    def __lt__(self,other):#Less Than
        return self.population < other.population

    def __eq__(self,other):#Equals
        return self.population == other.population

RJ = City("Rio de Janeiro", 1)
LA = City("Los Angeles", 2)
NY = City("New York", 3)
SP = City("São Paulo", 4)

cities = [LA,SP,NY,RJ]

cities.sort()
print(cities)
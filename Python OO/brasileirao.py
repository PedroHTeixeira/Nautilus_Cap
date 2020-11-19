# PYTHON OO 17/11/2020 17:00 Part-1 HW

class Team():

    def __init__(self,name,punctuation,matches,victories,draws,defeats):
        self.name = name
        self.punctuation = punctuation
        self.matches=matches
        self.victories=victories
        self.draws=draws
        self.defeats=defeats

    def __repr__(self):
        r = "The team {} has {} points. It has played {} matches and there were {} wins, {} draws and {} losses".format(self.name,self.punctuation,self.matches,self.victories,self.draws,self.defeats)
        return r

    def __add__(self,other):
        s=self.punctuation+other.punctuation
        return s

    def __gt__(self,other):
        gt = self.punctuation>other.punctuation
        return gt

    def __lt__(self,other):
        lt = self.punctuation<other.punctuation
        return lt
    
    def __sub__(self, other):
        s=self.punctuation-other.punctuation
        return s

team1=Team("Vasco",22,"19","6","4","9")
team2=Team("Flamengo",36,"21","10","6","5")
team3=Team("Fluminense",32,"21","9","5","7")
team4=Team("Botafogo",20,"20","3","11","6")
team5=Team("Goias",12,"19","2","6","11")
team6=Team("Atlético-Mg",38,"20","12","2","6")
team7=Team("Sport-Recife",25,"21","7","4","10")

teams=[team1,team2,team3,team4,team5,team6,team7]
teams.sort()
print(teams)
s= team2+team1
d= team2-team1
print("The sum of Vasco and Flamengo is :",s)
print("The subtraction between Vasco and Flamengo is :",d)
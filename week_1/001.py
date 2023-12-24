class PartyAnimal:
    x = 0
    name = ""
    # init constructor
    def __init__(self, name):
        self.name = name
        print("I am constrcuted ", self.name)
    
    
    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)

    
    # def __del__(self):
    #     print("I am destructed", self.x)
        
# inheritance
class FootBallFan(PartyAnimal):
    points = 0
    def touchDown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points)
    pass
p1  = PartyAnimal('lisa')
p2 = PartyAnimal('jenny')
p1.party() 

# init footballfan object 
p3 = FootBallFan('Jack')
p3.touchDown()
# print("Director", dir(p1))

# print("Type", type(p1))


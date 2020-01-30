# Use this file to define your Train class!
class Train:
    def __init__(self, model, age, origin, speed):
        self.model = model
        self.age = age
        self.origin = origin
        self.speed = speed
        self.durability = 100
        
    def birthday(self):
        self.age += 1
        self.durability -= 10
        if self.durability <= 0:
            print(self.model,"is no longer in operation.")
    
    def repair(self):
        self.durability += 10
        if self.durability >= 100:
            print(self.model,"is good as new!")
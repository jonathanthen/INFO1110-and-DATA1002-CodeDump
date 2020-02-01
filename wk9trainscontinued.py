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
            
    def is_older(self, object):
        if self.age > object.age:
            return True
        else:
            return False
        
    def travel_time(self, distance):
        daystaken = distance / self.speed
        return daystaken
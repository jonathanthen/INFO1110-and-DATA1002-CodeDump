class Box:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def get_weight(self):
        i = 0
        totalweight = 0
        while i < len(self.items):
            totalweight += self.items[i].weight
            i += 1
        return totalweight

class Item:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
class Box:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        if type(item) != Item:
            raise ValueError
        self.items.append(item)
    def get_weight(self):
        # Return weight of the box with all items inside
        total = 0
        i  = 0
        while i < len(self.items):
            total += self.items[i].weight
            i += 1
        return total

class Item:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


b = Box()
b.add_item(Item('Cat', 5))
b.add_item(Item("Nintendo Switch", 1))
b.add_item(Item('Potatoes', 2))

msg = 'The box weights {} kg'.format(b.get_weight())
print(msg) # The box weighs 8 kg
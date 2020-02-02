class Matryoshka:
    def __init__(self):
        self.child = None
        
    def set_child(self, child):
        self.child = child
    
    def count_descendants(self):
        if self.child == None:
            return 0
        else:
            return 1 + self.child.count_descendants()
class Circle:
    PI = 3.1415
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return Circle.PI * (self.radius)**2
        
    @staticmethod    
    def get_wiki_page():
        return "https://en.wikipedia.org/Circle"

c1 = Circle(2)
c2 = Circle(5)
c3 = Circle(4)

print(c1.get_area())
print(c2.get_area())
print(c3.get_area())

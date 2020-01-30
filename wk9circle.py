class Circle:
    PI = 3.1415
    def __init__(self, radius):
        self.radius = radius
    
    def get_wiki_page():
        return 'wiki.circle.com'
    
    def get_area(self):
        area = Circle.PI * (self.radius)**2
        return area
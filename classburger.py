class Review:
	def __init__(self, author, rating):
		self.author = author
		self.rating = rating
        

class Burger:
	def __init__(self, name, price):
		self.name = name
		self.price = price
		self.reviews = []
		self.listauthors = []
		self.average = 0

	def add_review(self, author, rating):
		x = Review(author, rating)
		self.reviews.append(x)

	def list_authors(self):
		if len(self.reviews) == 0:
			return self.reviews
		else:
			i = 0
			while i < len(self.reviews):
				self.listauthors.append(self.reviews[i].author)
				i += 1
			return self.listauthors
	
	def average_rating(self):
		self.total = 0
		self.count = 0
		if len(self.reviews) == 0:
			return 3
		else:
			j = 0
			while j < len(self.reviews):
				self.total += self.reviews[j].rating
				self.count += 1
				j += 1
			self.average = self.total / self.count
			return (self.average)

def top_burgers(burgers, minimum_rating):
    goodfood = []
    
    if type(burgers) != list or type(minimum_rating) != float:
        raise TypeError
        
    i = 0
    while i < len(burgers):
        if burgers[i].average >= minimum_rating:
            goodfood.append(burgers[i])
        i += 1
        
    return goodfood
				
cheeseburger = Burger('Cheeseburger', 4.99)
cheeseburger.add_review('Aaron', 2)
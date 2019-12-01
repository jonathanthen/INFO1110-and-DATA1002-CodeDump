class Book:
    def __init__(self, title, author, year, url):
        self.title = title
        self.author = author
        self.year = year
        self.url = url

# Is there a difference between variables title and self.title?
## title is the argument and is useless after everything.
##self.title is an instance and can be used persists through the class
#Does the __init__ method return anything? 
## It's for initializing the attributes of the class.
#How can we create a new Book object in Python? 
mybook = Book("Harry Potter", "J.K. Rowling", 1997, "www.hp.com")
mybook2 = Book("Pendragon", "D.J. MacHale", 2002, 'www.pendragon.com')
#What does the computer do to create this new object? 
#What data (or information) will each Book object store? 
#How can we access data stored in a Book object? 
print(mybook.title)
print(mybook.author)
print(mybook.year)
print(mybook.url)
#Would the text of a book be a suitable attribute?
print(mybook2.title)
print(mybook2.author)
print(mybook2.year)
print(mybook2.url)

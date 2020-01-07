class Animal:
    def __init__(self, name, age, a_type):
        self.name = name
        self.age = age
        self.a_type = a_type

    def get_name():
        return self.name

class Zoo:
    '''contains a list of Animal objects'''
    def __init__(self, animals):
        self.animals = animals

zoo = initialise_zoo()
names = iter(zoo)
print(names)
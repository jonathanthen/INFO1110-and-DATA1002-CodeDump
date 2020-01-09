class Pet:
    def __init__(self, name, age, species, trained):
        self.name = name
        self.nickname = []
        self.age = age
        self.species = species
        self.trained = trained
        if type(name) != str or len(name) == 0:
            raise ValueError
        if age < 0:
            raise ValueError
        if type(species) != str:
            raise ValueError
        if type(trained) != bool:
            raise ValueError

    def add_nickname(self, name):
        self.nickname.append(name)

    def has_nickname(name):
        i = 0
        while i < len(self.nickname):
            if self.nickname[i] == name:
                return True
        return False

p1 = ("Pear", 2, "Tigerean", True)
p1.add_nickname('Perry')
p1.add_nickname('Perrysaur')
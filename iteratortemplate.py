class People:
    def __intit(self, names):
        self.names = names

    def __iter__(self):
        return PeopleIterator(self.names)

class PeopleIterator:
    def __init__(self, names):
        self.names = names
        # the state of the iterator is defined as
        # the index of the list
        self.cursor = 0

    def __next__(self):
        # if the end of the list is reached, raise exception
        if self.cursor >= len(self.names):
            raise StopIteration("Reached end")

        # get the next element to return
        ret_val = self.names[self.cursor]

        # update the iterator state to the next element
        self.cursor += 1

        # return the value
        return ret_val

simpsons = People(["Armen", "Hans", "Lunchlady Doris"])
myiterator = iter(simpsons)
print(myiterator.__next__())
print(myiterator.__next__())
print(myiterator.__next__())
print(myiterator.__next__())
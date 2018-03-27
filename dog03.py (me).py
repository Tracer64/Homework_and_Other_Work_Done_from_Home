class Dog:
    """ This is the beginning of a class for the humble house dog """

    def __init__(self, name):
        self.name = name

    def add_weight(self, weight):
        self.weight = weight


d = Dog('Worf')
# d.name = "Worf"

x = Dog('Baxter')
# x.name = "Baxter"

x.add_weight(40)
# x.add_weight(40)

print(d.name)

print(x.name)
print(x.weight)

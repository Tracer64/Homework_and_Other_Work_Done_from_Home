class Cat:
    """ This is the beginning of a class for the humble house cat """
    
    def __init__(self, name):
        self.name = name

    def add_weight(self, weight):
        self.weight = weight


c = Cat('Fluffy is a cat and his name is Fluffy. He has a friend, a cat as well and his name is')
# c.name = "Fluffy"

x = Cat('Spike. Ironically, both cats weights are')
# x.name = "Spike"

x.add_weight(12)
# x.add_wieght(12)

print(c.name)

print(x.name)
print(x.weight)

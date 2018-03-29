class Dog:
    """ This is the beginning of a class for the humble house dog """

    def __init__(self, name):
        self.name = name

    def add_weight(self, weight):
        self.weight = weight

x = Dog('One of my dogs name is Baxter. His weight was 101 until a week ago when it increased to 110.')
#x.name = "Baxter"

d = Dog('One of my other dogs name is Worf, his weight was 40, until today when within a two week period, he gained 9 more pounds of weight and his total was then 49 lb.')
#d.name = "Worf"

x.add_weight(101)
#x.add_weight(101)

d.add_weight(40)
#x.addweight(40)

print(d.name)
print(d.weight)

print(x.name)
print(x.weight)

d.add_weight(9)
#d.add_weight(9) will add 9 to the original function for weight set at 40 to set the current weight to 49

x = weight(101)
x.add_weight(9)
#x.add_weight(9) will add 9 to the original function for weight set at 101 to set the current weight to 110

class Dog:
    """ This is the beginning of a class for the humble house dog """

    def __init__(self, name):
        self.name = name

    def add_weight(self, weight):
        self.weight = weight

x = Dog('Baxter')
#x.name = "Baxter"

d = Dog('Worf')
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

x.add_weight(1)
#x.add_weight(1) will add 1 to the original function for weight set at 101 to set the current weight to 110

#Don't forget to add the weight "CHANGES" remember that the changes didn't take effect when you last ran the program.

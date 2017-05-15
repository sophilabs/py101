class Vehicle:
    def __init__(self, cost):
        self.cost = cost

    def description(self):
        return "Vehicle cost is {}".format(self.cost)


car1 = Vehicle(12000)
car2 = Vehicle(5999.99)

print(car1.description())
print(car2.description())

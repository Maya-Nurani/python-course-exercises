import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def squared(self):
        print(math.pow(self.x, 2))

    def addGeneric(self, x=0, y=0):
        self.x += x
        self.y += y

p1 = Point(1, 1)
p2 = Point(2, 2)

p1.squared()
p1.addGeneric(x=3, y=2)

print('This is point1', p1)
print('This is point2', p2)

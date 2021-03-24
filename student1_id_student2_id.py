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


# --------------------------
class Rectangle:
    def __init__(self, x, y, width, height):
        Point.__init__(self, x, y)
        self.width = width
        self.height = height
        self.start_position = Point(x, y)

    def __str__(self):
        return str(self.width) + "," + str(self.height) + ", " + str(self.start_position)

    def get_area(self):
        return self.height * self.width

    def get_diag_length(self):
        diag_point = Point(self.x + self.width, self.y - self.height)
        # distance =

        return 2   # distance

obj = Rectangle(1,2, 5,6,)
print('This is Rectangle data:', obj)
print(Rectangle.get_area(obj))


'''
    def squared(self):
        print(math.pow(self.x, 2))

    def addGeneric(self, x=0, y=0):
        self.x += x
        self.y += y
'''

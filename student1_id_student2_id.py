import random


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    # not relevant for the project, this is example for a lesson
    def add_generic(self, x=0, y=0):
        self.x += x
        self.y += y

    def get_dist(self, x2, y2):
        distance = (((self.x - x2) ** 2 + (self.y - y2) ** 2) ** 0.5)
        return distance


p1 = Point(1, 1)
p2 = Point(4, 4)
p3 = Point(5, 4)

p1.add_generic(x=3, y=2)

print('This is point1', p1)
print('This is point2', p2)
print('The distance is:' + str(p1.get_dist(1, 1)))


# --------------------------
class Rectangle:
    def __init__(self, x, y, width, height):
        self.width = width
        self.height = height
        self.start_position = Point(x, y)

    def __str__(self):
        return str("Rectangle's width is:" + self.width.__str__() + ", Height is:"
                   + self.height.__str__() + ", Starting point:" + self.start_position.__str__())

    def get_area(self):
        return self.height * self.width

    def get_diag_length(self):
        diag_point = Point(self.start_position.x + self.width, self.start_position.y - self.height)
        return self.start_position.get_dist(diag_point.x, diag_point.y)

    def get_border_points(self):
        diag_point = Point(self.start_position.x + self.width, self.start_position.y - self.height)
        right_point = Point(self.start_position.x + self.width, self.start_position.y)
        left_point = Point(self.start_position.x, self.start_position.y - self.height)
        return [right_point, diag_point, left_point]


first_rectangle = Rectangle(0, 2, 2, 2)
print(first_rectangle)
print("Area of first rectangle =", first_rectangle.get_area())
print("Diag length of first rectangle =", first_rectangle.get_diag_length())


# --------------------------
class Triangle:
    def __init__(self, point1, point2, point3):
        self.topPoint = point1
        self.basePoint1 = point2
        self.basePoint2 = point3

    def __str__(self):
        return str("First point is:" + self.topPoint.__str__() + " Second point is:" + self.basePoint1.__str__()
                   + " Third point is:" + self.basePoint2.__str__())

    def get_vertices(self):
        l1 = [self.topPoint.__str__(), self.basePoint1.__str__(), self.basePoint2.__str__()]
        return l1

    def get_area(self):
        area = 0.5 * abs(self.topPoint.x * (self.basePoint1.y - self.basePoint2.y)
                         + self.basePoint1.x * (self.basePoint2.y - self.topPoint.y) +
                         self.basePoint2.x * (self.topPoint.y - self.basePoint1.y))
        return area
        # A = 0.5*[(x1(y2-y3)+x2(y3-y1)+x3(y1-y2)] equation for triangle's area calculation in XY pane

    def get_circumence(self):
        side1 = self.topPoint.get_dist(self.basePoint1.x, self.basePoint1.y)
        side2 = self.topPoint.get_dist(self.basePoint2.x, self.basePoint2.y)
        side3 = self.basePoint1.get_dist(self.basePoint2.x, self.basePoint2.y)
        return side1 + side2 + side3


myTriangle = Triangle(p1, p2, p3)
print(myTriangle)
print(myTriangle.get_vertices())
print(myTriangle.get_area())
print(myTriangle.get_circumence())

triangleList = []
rectangleList = []


# Generic function for random number
def random_num():
    return random.randint(1, 9)


# creates random triangles and rectangles and adds them to lists
for i in range(0, 5):
    randPoint1 = Point(random_num(), random_num())
    randPoint2 = Point(random_num(), random_num())
    randPoint3 = Point(random_num(), random_num())
    newTriangle = Triangle(randPoint1, randPoint2, randPoint3)
    newRectangle = Rectangle(randPoint1.x, randPoint1.y, random_num(), random.randint(1, 9))
    triangleList.append(newTriangle)
    rectangleList.append(newRectangle)

print(rectangleList[0])
print(triangleList[0])

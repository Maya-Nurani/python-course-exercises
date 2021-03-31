class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    # not relevant for the project, this is example for a lesson
    def addGeneric(self, x=0, y=0):
        self.x += x
        self.y += y

    def get_dist(self,x2,y2):
        distance = (((self.x-x2)**2+(self.y-y2)**2)**0.5)
        return distance


p1 = Point(1, 1)
p2 = Point(2, 2)
p3 = Point(3,3)

p1.addGeneric(x=3, y=2)

print('This is point1', p1)
print('This is point2', p2)
print('The distance is:'+ str(p1.get_dist(1,1)))


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
        # distance = # according to distance between points formula

        return 0  # distance


first_rectangle = Rectangle(1, 2, 5, 6)
print('This is Rectangle data:', first_rectangle)
print(Rectangle.get_area(first_rectangle))


# --------------------------
class Triangle:
    def __init__(self,point1,point2,point3):
        self.topPoint = point1
        self.basePoint1 = point2
        self.basePoint2 = point3
        self.baseLength = point2.get_dist(point3.x,point3.y)
        self.height = int(point1.y-point2.y)

    def __str__(self):
        return str("First point is:"+self.topPoint.__str__()+" Second point is:"+self.basePoint1.__str__()+" Third point is:"+self.basePoint2.__str__())

    def get_vertices(self):
        l1 = [self.topPoint.__str__(),self.basePoint1.__str__(),self.basePoint2.__str__()]
        return l1

    def get_area(self):
        area = ((self.height)*(self.baseLength))/2
        return area

    def get_circumence(self):
        side1 = self.topPoint.get_dist(self.basePoint1.x,self.basePoint1.y)
        side2 = self.topPoint.get_dist(self.basePoint2.x,self.basePoint2.y)
        return side1+side2+self.baseLength

myTriangle = Triangle(p1, p2, p3)
print(myTriangle)
print(myTriangle.get_vertices())
print(myTriangle.baseLength)
print(myTriangle.height)
print(myTriangle.get_area())
print(myTriangle.get_circumence())




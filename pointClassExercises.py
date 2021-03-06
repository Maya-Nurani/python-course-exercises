#Submision number 1
import random


# Student 1 - Laly Datsyuk
# Student 2 - Maya Nurani

# --------------------------Point--------------------------#
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def get_dist(self, x2, y2):
        distance = (((self.x - x2) ** 2 + (self.y - y2) ** 2) ** 0.5)
        return distance


# --------------------------Rectangle--------------------------#
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
        return [self.start_position, right_point, diag_point, left_point]

    def add_value_height(self, value):
        self.height = self.height + value

    def add_value_width(self, value):
        self.width = self.width + value


# --------------------------Triangle--------------------------#
class Triangle:
    def __init__(self, point1, point2, point3):
        self.p1 = point1
        self.p2 = point2
        self.p3 = point3

    def __str__(self):
        return str(
            "Triangle: First point is:" + self.p1.__str__() + " Second point is:" + self.p2.__str__()
            + " Third point is:" + self.p3.__str__())

    def get_vertices(self):
        l1 = [self.p1.__str__(), self.p2.__str__(), self.p3.__str__()]
        return l1

    def get_area(self):
        area = 0.5 * abs(self.p1.x * (self.p2.y - self.p3.y)
                         + self.p2.x * (self.p3.y - self.p1.y) +
                         self.p3.x * (self.p1.y - self.p2.y))
        return area
        # A = 0.5*[(x1(y2-y3)+x2(y3-y1)+x3(y1-y2)] equation for triangle's area calculation in XY pane

    def get_circumence(self):
        side1 = self.p1.get_dist(self.p2.x, self.p2.y)
        side2 = self.p1.get_dist(self.p3.x, self.p3.y)
        side3 = self.p2.get_dist(self.p3.x, self.p3.y)
        return side1 + side2 + side3


# --------------------------Part B--------------------------#

# Function for random number
def random_num():
    return random.randint(0, 9)


# Function for random point object
def random_point():
    return Point(random_num(), random_num())


# Part B - section 1 - create lists of random objects
triangleList = []
rectangleList = []

# Creates random triangles and rectangles and adds them to lists
for i in range(0, 5):
    newTriangle = Triangle(random_point(), random_point(), random_point())
    newRectangle = Rectangle(random_point().x, random_point().y, random_num(), random_num())
    triangleList.append(newTriangle)
    rectangleList.append(newRectangle)

# Create 1 list for both Rectangle and Triangle objects
formList = rectangleList + triangleList

# This function get list of shapes and print the areas of all items
def print_list_by_area(listToPrint):
    for shape in listToPrint:
        print(shape.get_area())

# This function get list of shapes and print the areas of all items
def print_list_shapes(listToPrint):
    for shape in listToPrint:
        print(shape)


# Part B - section 2 - sorting methods
# Selection sort (by area)
def selection_sort_objects(inputList):
    for i in range(len(inputList)):
        min = i
        for j in range(i + 1, len(inputList)):
            if inputList[min].get_area() > inputList[j].get_area():
                min = j
        inputList[i], inputList[min] = inputList[min], inputList[i]
    return inputList


# Bubble sort (by area)
def bubble_sort_objects(inputList):
    for n in range(len(inputList)):
        for index in range(len(inputList) - n - 1):
            if inputList[index].get_area() > inputList[index + 1].get_area():
                inputList[index], inputList[index + 1] = inputList[index + 1], inputList[index]
    return inputList


# This function get sort method and list of shapes and return a sort list
def sort_objects(sortType, inputList):
    if sortType == 'bubble':
        inputList = bubble_sort_objects(inputList)
    elif sortType == 'selection':
        inputList = selection_sort_objects(inputList)
    return inputList

# Send the list to sort function
sortType = ['bubble', 'selection']
formList = sort_objects(sortType[1], formList)

print("after sort")
# Part B - section 3 - print sorted list
print_list_by_area(formList)


# Part B - section 4 - add Rectangle to the list while keeping the order
def add_rectangle(x, y, width, height, list):
    newRectangle = Rectangle(x, y, width, height)
    area = newRectangle.get_area()
    print("The area of the new Rectangle", area)
    # Adding the Rectangle to the right place
    isAdded = False
    for i in range(len(list) - 1):
        if list[i].get_area() <= area <= list[i + 1].get_area():
            list.insert(i + 1, newRectangle)
            isAdded = True
            break;
    # If the new area bigger than all existence areas in the list - we will add it at the end of the list
    if isAdded == False:
        list.insert(len(list) + 1, newRectangle)


add_rectangle(random_point().x, random_point().y, random_num(), random_num(), formList)

# Part B - section 5 - print sorted list
# Print list (by area) after adding new Rectangle
print("print list (by area) after adding new Rectangle")
print_list_by_area(formList)
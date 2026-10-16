from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


# Child class 1
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


# Child class 2
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


# Create objects
r = Rectangle(10, 5)
c = Circle(7)

print("Area of Rectangle:", r.area())
print("Area of Circle:", c.area())
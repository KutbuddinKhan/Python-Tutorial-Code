# from abc import ABCMeta, abstractmethod
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def printArea(self):
        return 0

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4

    def __init__(self):
        self.length = 6
        self.breadth = 5

    def printArea(self):
        return self.length * self.breadth

rect1 = Rectangle()
print(rect1.printArea())
# try1 = Shape()

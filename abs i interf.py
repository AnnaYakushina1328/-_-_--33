#использование абстрактных функций

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

    def perimeter(self):
        return 4 * self.side_length

circle = Circle(5)
square = Square(4)

print("Площадь круга:", circle.area())
print("Периметр круга:", circle.perimeter())

print("Площадь квадрата:", square.area())
print("Периметр квадрата:", square.perimeter())


# использование интерфейсов

from abc import ABC, abstractmethod
import math

class ShapeInterface(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Shape(ShapeInterface):
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

    def perimeter(self):
        return 4 * self.side_length

circle = Circle(5)
square = Square(4)

print("Площадь круга:", circle.area())
print("Периметр круга:", circle.perimeter())

print("Площадь квадрата:", square.area())
print("Периметр квадрата:", square.perimeter())

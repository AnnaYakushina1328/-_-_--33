# класс Point представляет точку с координатами x и y. Мы перегружаем операторы +, - и *, чтобы можно было выполнять арифметические операции с объектами этого класса.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Point(self.x * scalar, self.y * scalar)

    def __str__(self):
        return f"({self.x}, {self.y})"

# Создаем две точки
point1 = Point(3, 4)
point2 = Point(1, 2)

# Перегрузка оператора сложения (+)
added_point = point1 + point2
print("Сумма точек:", added_point)

# Перегрузка оператора вычитания (-)
subtracted_point = point1 - point2
print("Разность точек:", subtracted_point)

# Перегрузка оператора умножения (*)
multiplied_point = point1 * 2
print("Умножение точки на скаляр:", multiplied_point)

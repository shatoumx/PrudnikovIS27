# Задача 1: Создание класса "Товар"
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Название: {self.name}, Цена: {self.price}, Количество: {self.quantity}")


# Задача 2: Создание базового класса "Фигура" и классов "Прямоугольник" и "Квадрат"
class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Rectangle(Shape):
    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Square(Shape):
    def area(self):
        return self.width * self.width

    def perimeter(self):
        return 4 * self.width


# Пример использования классов
# Создание объекта класса "Товар"
product1 = Product("Книга", 500, 10)
product1.display_info()

# Создание объектов классов "Прямоугольник" и "Квадрат"
rectangle = Rectangle(5, 10)
print("Площадь прямоугольника:", rectangle.area())
print("Периметр прямоугольника:", rectangle.perimeter())

square = Square(5, 5)
print("Площадь квадрата:", square.area())
print("Периметр квадрата:", square.perimeter())

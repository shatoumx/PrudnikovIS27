# Создайте класс "Человек", который содержит информацию о имени, возрасте и поле.
# Создайте классы "Мужчина" и "Женщина", которые наследуются от класса
# "Человек". Каждый класс должен иметь метод, который выводит информацию о
# поле объекта.
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")


class Man(Person):
    def __init__(self, name, age):
        super().__init__(name, age, "Male")

    def display_info(self):
        print("Man's Information:")
        super().display_info()


class Woman(Person):
    def __init__(self, name, age):
        super().__init__(name, age, "Female")

    def display_info(self):
        print("Woman's Information:")
        super().display_info()


person1 = Person("Alex", 30, "Male")
print("Person's Information:")
person1.display_info()
print("----------------------")

man1 = Man("John", 25)
man1.display_info()
print("----------------------")

woman1 = Woman("Emma", 28)
woman1.display_info()

# Приложение ВЫДАЧА КРЕДИТОВ для некоторой организации. БД должна
# содержать таблицу Клиент со следующей структурой записи: ФИО клиента, ФИО
# сотрудника банка, срок кредита, процент кредита, сумма кредита

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def info(self):
        return f"Name: {self.name}, Species: {self.species}"


animal_list = [Animal("Tiger", "Predator"), Animal("Elephant", "Herbivore"),
               Animal("Cheetah", "Predator")]


def get_animal(valid_animals):
    while True:
        print("Available animals:")
        for i, animal in enumerate(valid_animals):
            print(f"{i + 1}: {animal.name}")
        choice = input("Enter the animal number (1-3): ")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= 3:
                return valid_animals[choice - 1]
            else:
                print("Invalid animal number. Please choose a number between 1 and 3.")
        else:
            print("Please enter a numerical value.")


chosen_animal = get_animal(animal_list)

print(chosen_animal.info())

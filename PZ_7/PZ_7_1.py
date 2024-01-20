# Дана строка, изображающая целое положительное число. Вывести сумму цифр этого числа.
def sum_of_digits(number):
    # Преобразуем число в строку
    number_str = str(number)

    # Инициализируем сумму цифр
    digit_sum = 0

    # Итерируемся по каждой цифре в строке
    for digit in number_str:
        # Преобразуем цифру обратно в число и добавляем к сумме
        digit_sum += int(digit)

    # Возвращаем сумму цифр
    return digit_sum


while True:
    try:
        number = int(input("Введите ваше число: "))
    except ValueError:
        print('Ошибка')
        continue
    break
result = sum_of_digits(number)
print(f"Сумма цифр числа {number} равна {result}")

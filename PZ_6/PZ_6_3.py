# Дано множество А из N точек на плоскости и точка В (точки заданы своими
# координатами х, у). Найти точку из множества А, наиболее близкую к точке В.
# Расстожше R между точками с координатами (XI, у) и (м, у) вычисляется по
# формуле:
# R = √(х2 - х1):2 + (у2 - у1)^2.
# Для хранения данных о каждом наборе точек следует использовать по два списка: первый
# список для хранения абсцисс, второй — для хранения ординат.
import math


def find_closest_point(A):
    closest_point = [0, 0]  # Изначально считаем точку с нулевыми координатами ближайшей
    closest_distance = math.inf  # Изначально считаем бесконечную дистанцию

    for i in range(len(A[0])):
        x = A[0][i]
        y = A[1][i]

        # Проверка
        if x >= 0 and y >= 0 or x <= 0 and y <= 0:
            distance = math.sqrt(x ** 2 + y ** 2)  # Вычисляем расстояние до начала координат

            if distance < closest_distance:
                closest_distance = distance
                closest_point = [x, y]

    return closest_point


A = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
closest_point = find_closest_point(A)
print("Ближайшая точка:", closest_point)

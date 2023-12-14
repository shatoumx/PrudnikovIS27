# Описать процедуру Mean(X, Y, AMean), вычисляющую среднее арифметическое AMean = (X + Y)/2 и среднее геометрическое
# GMean = y/X Y двух положительных чисел X и Y (X и Y - входные), AMean и GMean - выходные параметры вещественного типа)
# С помощью этой функции найти среднее арифметическое и среднее геометрическое для пар (A, B), (A, C), (A, D), если даны
# A, B, C, D.
print('Вторая задача')
import math


def Mean(X, Y, AMean, GMean):
    AMean[0] = (X + Y) / 2
    GMean[0] = math.sqrt(X * Y)


while True:
    try:
        A = float(input("A = "))
        B = float(input("B = "))
        C = float(input("C = "))
        D = float(input("D = "))
    except ValueError:
        print('Ошибка')
        continue
    break

AMean, GMean = [0], [0]

Mean(A, B, AMean, GMean)
print(AMean[0], ' ', GMean[0])

Mean(A, C, AMean, GMean)
print(AMean[0], ' ', GMean[0])

Mean(A, D, AMean, GMean)
print(AMean[0], ' ', GMean[0])

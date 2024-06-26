# Дано вещественное число X (X<1) и целое число N (>0).Найти значение выражения 1 - X*2/2 + X*3/3 - ... + (-1)n-1X*N/N.
# Полученное число является приближённым значением функции ln в точке 1 + X. #

import math

X = input("Введите вещественное число : ")
N = input("Введите целое число : ")
a = 0
try:
    X = float(X)
    N = int(N)
    for i in range(1, N+1):
        a += ((-1)**(i-1)) * (X**i) / i
    b = a
    print("Приближенное значение:", b)
    print("Точное значение:", math.log(1 + X))
except:
    print("Что-то пошло не так")
# Дан список размера N и целые числа K и L (1 < K ≤ L ≤ N). Найти среднее арифметическое всех элементов массива, кроме
# элементов с номерами от K до L включительно.
N = [1, 2, 3, 4, 5]
while True:
    try:
        k = int(input('Введите число k: '))
        l = int(input('Введите число l: '))
    except ValueError:
        print('Ошибка')
        continue
    break

r = [x for i, x in enumerate(N, 1) if i < k or i > l]
print(r)
print(sum(r) / len(r))

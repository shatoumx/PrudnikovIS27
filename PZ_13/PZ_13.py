# В матрице найти минимальный элемент в предпоследнем столбце
matrix = [
    [3, 8, 5, 12],
    [4, 7, 1, 9],
    [10, 6, 11, 2],
    [8, 3, 5, 7]
]

min_in_second_last_column = min(row[-2] for row in matrix)

print("Минимальный элемент в предпоследнем столбце:", min_in_second_last_column)

for i, row in enumerate(matrix):
    if i % 2 != 0:  # Если номер строки нечетный
        average = sum(row) / len(row)
        print(f"Среднее арифметическое для строки {i + 1}: {average}")

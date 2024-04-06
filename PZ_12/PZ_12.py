# Даны текущие оценки студента по дисциплине «Основы программирования» за
# месяц. Необходимо найти количество «2», «3», «4» и «5», полученных студентом, и
# определить итоговую оценку за месяц
grades = [2, 4, 5, 3, 4, 5, 5, 4, 3, 2]

count_2 = grades.count(2)
count_3 = grades.count(3)
count_4 = grades.count(4)
count_5 = grades.count(5)

final_grade = (count_2 * 2 + count_3 * 3 + count_4 * 4 + count_5 * 5) / len(grades)

print("Количество 2:", count_2)
print("Количество 3:", count_3)
print("Количество 4:", count_4)
print("Количество 5:", count_5)
print("Итоговая оценка", final_grade)

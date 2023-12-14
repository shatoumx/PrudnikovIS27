# Дано число А(>1). Вывести наибольшее из целых чисел К, для которых сумма 1 + 1/2 + ... + 1/K будет меньше А, и саму
# эту суммy
print('Вторая задача')


def find_largest_sum(A):
    K = 1
    sum = 0
    while sum < A:
        K += 1
        sum += 1 / K
    return K - 1, sum - 1 / K


A = int(input("Введите ваше число: "))
print('A =', A)
largest_K, sum = find_largest_sum(A)
print("Наибольшее K: ", largest_K)
print("Сумма: ", sum)

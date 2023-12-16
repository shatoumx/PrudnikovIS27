# Дана строка, состоящая из русских слов, разделенных пробелами (одним или несколькими). Найти длину самого длинного
# слова.
def find_longest_word_length(string):
    words = string.split()  # Разделяем строку на слова по пробелам
    longest_word_length = 0  # Переменная для хранения длины самого длинного слова

    for word in words:
        if len(word) > longest_word_length:
            longest_word_length = len(word)

    return longest_word_length


input_string = input('Введите слово: ')
result = find_longest_word_length(input_string)
print(result)

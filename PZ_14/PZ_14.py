# ¬ исходном текстовом файле(Dostoevsky.txt) найти все годы де€тельности писател€
# (например, 1821 года, 1837 год, 1843 году и так далее по всему тексту). ѕосчитать
# количество полученных элементов.

import re

with open('Dostoevsky.txt', 'r', encoding='utf-8') as file:
    text = file.read()

years = re.findall(r'\b\d{4}\b', text)

print(years)
print(len(years))

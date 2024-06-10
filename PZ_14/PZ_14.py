# � �������� ��������� �����(Dostoevsky.txt) ����� ��� ���� ������������ ��������
# (��������, 1821 ����, 1837 ���, 1843 ���� � ��� ����� �� ����� ������). ���������
# ���������� ���������� ���������.

import re

with open('Dostoevsky.txt', 'r', encoding='utf-8') as file:
    text = file.read()

years = re.findall(r'\b\d{4}\b', text)

print(years)
print(len(years))

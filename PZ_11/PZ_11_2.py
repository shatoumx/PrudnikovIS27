# -*- coding: cp1251 -*-

# �� ������������� ���������� ����� (text18-22.txt) ������� �� ����� ��� ����������, ���������� ���� � �������
# ��������. ������������ ����� ����, � ������� ��������� ����� � ������������ ����� �������������� ������� �������
# ������ ������ �� ��������� ������.

with open('text18-22.txt', 'r') as file:
    stih = file.read()
    print(stih)

    kolvo_verh_reg = sum(1 for char in stih if char.isupper())
    print(f"���������� ���� � ������� ��������: {kolvo_verh_reg}")

    lines = stih.split('\n')
    if len(lines) >= 3:
        third_line = lines[2]
        chisl_code = ' '.join(str(ord(char)) for char in third_line)

    with open('3 ������ � ��������� ����.txt', 'w') as v_chisl_code:
        v_chisl_code.write('\n'.join([chisl_code[i:i + 12] for i in range(0, len(chisl_code), 12)]))

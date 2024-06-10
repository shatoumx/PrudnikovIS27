# Приложение ВЫДАЧА КРЕДИТОВ для некоторой организации. БД должна
# содержать таблицу Клиент со следующей структурой записи: ФИО клиента, ФИО
# сотрудника банка, срок кредита, процент кредита, сумма кредита

import sqlite3

conn = sqlite3.connect('credit_app.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Client (
id INTEGER PRIMARY KEY AUTOINCREMENT,
client_name TEXT,
banking_employee_name TEXT,
loan_term INTEGER,
loan_interest REAL,
loan_amount REAL
)
''')

client_data = [
    ('Ivanov Ivan Ivanovich', 'Petrov Petr Petrovich', 12, 10.5, 10000.0),
    ('Sidorov Alexey Pavlovich', 'Ivanova Maria Vladimirovna', 24, 12.0, 15000.0),
    ('Petrova Olga Sergeevna', 'Smirnov Andrey Alexandrovich', 6, 8.0, 8000.0),
    ('Kozlov Dmitriy Sergeevich', 'Nikitina Elena Viktorovna', 18, 11.5, 12000.0)
]

for client in client_data:
    cursor.execute('''
INSERT INTO Client (client_name, banking_employee_name, loan_term, loan_interest, loan_amount)
VALUES (?, ?, ?, ?, ?)
''', client)

conn.commit()

cursor.execute('SELECT * FROM Client')
rows = cursor.fetchall()

print("{:<5} {:<20} {:<25} {:<10} {:<15} {:<15}".format('ID', 'Client Name', 'Banking Employee Name',
                                                        'Loan Term', 'Loan Interest', 'Loan Amount'))
for row in rows:
    print("{:<5} {:<20} {:<25} {:<10} {:<15} {:<15}".format(row[0], row[1], row[2], row[3], row[4], row[5]))

conn.close()

# Удаление
import os
os.remove('credit_app.db')

import tkinter as tk


def find_hundreds_digit():
    num = int(entry.get())

    if num <= 999:
        result_label.config(text="Число должно быть больше 999")
    else:
        hundreds_digit = (num // 100) % 10
        result_label.config(text=f"Цифра сотен: {hundreds_digit}")


# Создаем графический интерфейс
root = tk.Tk()
root.title("Поиск цифры сотен")
root.geometry("300x150")
root.resizable(width=False, height=False)

label = tk.Label(root, text="Введите число больше 999:")
label.pack()

entry = tk.Entry(root, width=20)
entry.pack()

find_button = tk.Button(root, text="Найти цифру сотен", command=find_hundreds_digit)
find_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()

# В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
# его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
# приближенный к оригиналу (см. таблицу 1)

import tkinter as tk
from tkinter import ttk


def submit_form():
    print("Form submitted!")


root = tk.Tk()
root.title("Certificate Self Service Portal")
root.geometry("480x550")
root.resizable(width=False, height=False)

elements = [
    {"label": "Fill out the form to get a certificate", "widget": ttk.Label(root, font=("Arial", 12))},
    {"label": "Requester", "widget": ttk.Entry(root, width=30)},
    {"label": "Short Name", "widget": ttk.Entry(root, width=30)},
    {"label": "Email", "widget": ttk.Entry(root, width=30)},
    {"label": "Organization", "widget": ttk.Entry(root, width=30)},
    {"label": "Country", "widget": ttk.Combobox(root, width=30, values=["Austria", "USA"])},
    {"label": "IPv4 Address", "widget": ttk.Entry(root, width=30)},
    {"label": "Hostname", "widget": ttk.Entry(root, width=30)},
    {"label": "FQDN", "widget": ttk.Entry(root, width=30)},
    {"label": "Description", "widget": tk.Text(root, height=4, width=30)}
]

for i, element in enumerate(elements):
    label = ttk.Label(root, text=element["label"])
    widget = element["widget"]
    label.grid(row=i, column=0, padx=10, pady=10)
    widget.grid(row=i, column=1, padx=10, pady=10)

submit_button = ttk.Button(root, text="Submit Form", command=submit_form)
submit_button.grid(row=len(elements), column=1, padx=10, pady=10)

root.mainloop()

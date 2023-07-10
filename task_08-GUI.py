import csv
import tkinter as tk
from tkinter import messagebox, ttk
import os


def load_contacts(filename):
    contacts = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                contacts.append(row)
    return contacts


def save_contacts(filename, contacts):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        for contact in contacts:
            writer.writerow(contact)


def add_contact():
    last_name = last_name_entry.get()
    first_name = first_name_entry.get()
    middle_name = middle_name_entry.get()
    phone_number = phone_number_entry.get()

    if not last_name or not first_name or not phone_number:
        messagebox.showerror(
            "Ошибка", "Пожалуйста, введите необходимую информацию.")
    else:
        contacts.append([last_name, first_name, middle_name, phone_number])
        save_contacts('contacts.txt', contacts)
        messagebox.showinfo("Успех", "Контакт успешно добавлен.")
        clear_entries()
        load_contacts_treeview()


def search_contacts():
    search_term = search_entry.get().lower()
    search_results = []
    for contact in contacts:
        if any(search_term in field.lower() for field in contact):
            search_results.append(contact)
    load_contacts_treeview(search_results)


def delete_contact():
    selected_item = contacts_treeview.focus()
    if selected_item:
        confirmed = messagebox.askyesno(
            "Подтверждение", "Вы уверены, что хотите удалить контакт?")
        if confirmed:
            contact = contacts_treeview.item(selected_item)['values']
            contacts.remove(contact)
            save_contacts('contacts.txt', contacts)
            messagebox.showinfo("Успех", "Контакт успешно удален.")
            load_contacts_treeview()
    else:
        messagebox.showerror(
            "Ошибка", "Пожалуйста, выберите контакт для удаления.")


def clear_entries():
    last_name_entry.delete(0, tk.END)
    first_name_entry.delete(0, tk.END)
    middle_name_entry.delete(0, tk.END)
    phone_number_entry.delete(0, tk.END)


def load_contacts_treeview(filtered_contacts=None):
    contacts_treeview.delete(*contacts_treeview.get_children())
    contacts_to_display = filtered_contacts if filtered_contacts else contacts
    for contact in contacts_to_display:
        contacts_treeview.insert('', tk.END, values=contact)


# Проверка наличия файла и создание, если он отсутствует
filename = 'contacts.txt'
if not os.path.exists(filename):
    with open(filename, 'w'):  # Создание пустого файла
        pass

contacts = load_contacts(filename)

root = tk.Tk()
root.title("Телефонная Книга")

# Фрейм для добавления контакта
add_contact_frame = tk.LabelFrame(root, text="Добавить контакт")
add_contact_frame.pack(padx=10, pady=10)

last_name_label = tk.Label(add_contact_frame, text="Фамилия:")
last_name_label.grid(row=0, column=0, sticky=tk.W)
last_name_entry = tk.Entry(add_contact_frame)
last_name_entry.grid(row=0, column=1, padx=5, pady=5)

first_name_label = tk.Label(add_contact_frame, text="Имя:")
first_name_label.grid(row=1, column=0, sticky=tk.W)
first_name_entry = tk.Entry(add_contact_frame)
first_name_entry.grid(row=1, column=1, padx=5, pady=5)

middle_name_label = tk.Label(add_contact_frame, text="Отчество:")
middle_name_label.grid(row=2, column=0, sticky=tk.W)
middle_name_entry = tk.Entry(add_contact_frame)
middle_name_entry.grid(row=2, column=1, padx=5, pady=5)

phone_number_label = tk.Label(add_contact_frame, text="Номер телефона:")
phone_number_label.grid(row=3, column=0, sticky=tk.W)
phone_number_entry = tk.Entry(add_contact_frame)
phone_number_entry.grid(row=3, column=1, padx=5, pady=5)

add_button = tk.Button(add_contact_frame, text="Добавить", command=add_contact)
add_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Фрейм для поиска
search_frame = tk.LabelFrame(root, text="Поиск")
search_frame.pack(padx=10, pady=10)

search_label = tk.Label(search_frame, text="Поисковый запрос:")
search_label.grid(row=0, column=0, sticky=tk.W)
search_entry = tk.Entry(search_frame)
search_entry.grid(row=0, column=1, padx=5, pady=5)

search_button = tk.Button(search_frame, text="Поиск", command=search_contacts)
search_button.grid(row=0, column=2, padx=5, pady=5)

# Вывод контактов в виде таблицы
contacts_treeview = ttk.Treeview(root, columns=(1, 2, 3, 4), show="headings")
contacts_treeview.column(1, width=100)
contacts_treeview.column(2, width=100)
contacts_treeview.column(3, width=100)
contacts_treeview.column(4, width=150)
contacts_treeview.heading(1, text="Фамилия")
contacts_treeview.heading(2, text="Имя")
contacts_treeview.heading(3, text="Отчество")
contacts_treeview.heading(4, text="Номер телефона")
contacts_treeview.pack(padx=10, pady=10)

# Кнопка удаления контакта
delete_button = tk.Button(root, text="Удалить контакт", command=delete_contact)
delete_button.pack(pady=10)

load_contacts_treeview()

root.mainloop()

import os


def load_contacts(filename):
    contacts = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                contact_data = line.strip().split(',')
                contacts.append(contact_data)
    return contacts


def save_contacts(filename, contacts):
    with open(filename, 'w') as file:
        for contact in contacts:
            file.write(','.join(contact) + '\n')


def display_contacts(contacts):
    if not contacts:
        print("Справочник пуст.")
    else:
        print("Контакты:")
        for contact in contacts:
            print("Фамилия:", contact[0])
            print("Имя:", contact[1])
            print("Отчество:", contact[2])
            print("Номер телефона:", contact[3])
            print()


def search_contacts(contacts):
    search_term = input(
        "Введите фамилию, имя, отчество или номер телефона для поиска: ")
    search_results = []
    for contact in contacts:
        if any(search_term.lower() in field.lower() for field in contact):
            search_results.append(contact)
    display_contacts(search_results)


def update_contact(contacts):
    search_term = input(
        "Введите фамилию или имя для поиска контакта, которого нужно изменить: ")
    found_contacts = []
    for contact in contacts:
        if any(search_term.lower() in field.lower() for field in contact):
            found_contacts.append(contact)
    if found_contacts:
        print("Найденные контакты:")
        for i, contact in enumerate(found_contacts):
            print(i+1, "- Фамилия:", contact[0])
            print("Имя:", contact[1])
            print("Отчество:", contact[2])
            print("Номер телефона:", contact[3])
            print()
        choice = int(
            input("Введите номер контакта, который нужно изменить: ")) - 1
        if 0 <= choice < len(found_contacts):
            contact = found_contacts[choice]
            print("Изменение контакта:")
            contact[0] = input("Введите новую фамилию: ")
            contact[1] = input("Введите новое имя: ")
            contact[2] = input("Введите новое отчество: ")
            contact[3] = input("Введите новый номер телефона: ")
            save_contacts('contacts.txt', contacts)
            print("Контакт успешно изменен!")
        else:
            print("Неверный выбор контакта.")
    else:
        print("Контакты не найдены.")


def delete_contact(contacts):
    search_term = input(
        "Введите фамилию или имя для поиска контакта, который нужно удалить: ")
    found_contacts = []
    for contact in contacts:
        if any(search_term.lower() in field.lower() for field in contact):
            found_contacts.append(contact)
    if found_contacts:
        print("Найденные контакты:")
        for i, contact in enumerate(found_contacts):
            print(i+1, "- Фамилия:", contact[0])
            print("Имя:", contact[1])
            print("Отчество:", contact[2])
            print("Номер телефона:", contact[3])
            print()
        choice = int(
            input("Введите номер контакта, который нужно удалить: ")) - 1
        if 0 <= choice < len(found_contacts):
            contact = found_contacts[choice]
            contacts.remove(contact)
            save_contacts('contacts.txt', contacts)
            print("Контакт успешно удален!")
        else:
            print("Неверный выбор контакта.")
    else:
        print("Контакты не найдены.")


def main_menu():
    contacts = load_contacts('contacts.txt')
    while True:
        print("Меню:")
        print("1. Просмотреть контакты")
        print("2. Добавить контакт")
        print("3. Поиск контакта")
        print("4. Изменить контакт")
        print("5. Удалить контакт")
        print("6. Выход")
        choice = input("Введите номер пункта меню: ")
        print()
        if choice == '1':
            display_contacts(contacts)
        elif choice == '2':
            last_name = input("Введите фамилию: ")
            first_name = input("Введите имя: ")
            middle_name = input("Введите отчество: ")
            phone_number = input("Введите номер телефона: ")
            contacts.append([last_name, first_name, middle_name, phone_number])
            save_contacts('contacts.txt', contacts)
            print("Контакт успешно добавлен!")
        elif choice == '3':
            search_contacts(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
        print()


main_menu()

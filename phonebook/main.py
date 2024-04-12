"""from functions import (
    add_contact,
    delete_contact,
    find_contact,
    show_all_contacts,
    ask_contact,
)"""


def ask_contact(contacts):
    name = input("Введите имя: ")
    middle_name = input("Введите отчество: ")
    second_name = input("Введите фамилию: ")
    number = input("Введите номер телефона: ")
    contacts = {
        "Имя": name,
        "Отсечтво": middle_name,
        "Фамилия": second_name,
        "Номер телефона": number,
    }

    print(f"Контакт {name} добавлен.")
    return contacts


def add_contact(phone_book):
    contact = ask_contact
    with open("address_book.txt", "a") as file:
        for value in contact.values():
            file.write(str(value))
        file.write("\n")
    return True


def delete_contact(phone_book, name):
    if name in phone_book:
        del phone_book[name]
        print(f"Контакт {name} удален.")
    else:
        print(f"Контакт {name} не найденю")


def find_contact(phone_book, name):
    if name in phone_book:
        print(f"{name}: {phone_book[name]}")
    else:
        print(f"Контакт {name} не найденю")


def show_all_contacts(phone_book, name, number):
    if phone_book:
        for name, number in phone_book.items():
            print(f"{name}: {number}")
        else:
            print("Телефонная книга пуста:")


def main_menu():
    phone_book = {}
    while True:
        print("\n1. Добавить контакт")
        print("2. Удалить контакт")
        print("3. Найти контакт")
        print("4. Показать все контакты")
        print("5. Выйти")
        choice = input("Выберите действие: ")

        if choice == "1":
            add_contact(phone_book)
        elif choice == "2":
            name = input("Введите имя для удаления: ")
            delete_contact(phone_book, name)
            print("Контакт удален. ")
        elif choice == "3":
            name = input("Введите имя: ")
            find_contact(phone_book, name)
        elif choice == "4":
            name = input("Введите имя: ")
            show_all_contacts(phone_book)
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")


if __name__ == "__main__":
    main_menu()

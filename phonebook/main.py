"""from functions import (
    add_contact,
    delete_contact,
    find_contact,
    show_all_contacts,
    ask_contact, 
)"""


def ask_contact(contacts):  # спрашиваем данные контакта
    name = input("Введите имя: ")
    middle_name = input("Введите отчество: ")
    second_name = input("Введите фамилию: ")
    number = input("Введите номер телефона: ")
    contacts = {
        "Имя": name,
        "Отчество": middle_name,
        "Фамилия": second_name,
        "Номер телефона": number,
    }

    print(f"Контакт {name} добавлен.", end="\n\n")
    return contacts


def add_contact(phone_book):  # добаляем контакт
    contact = ask_contact(phone_book)
    with open("address_book.txt", "a", encoding="utf-8") as file:
        for value in contact.values():
            file.write(str(value + "  "))
        file.write("\n")
    return True


def find_contact(phone_book, name):  # ишем еонтакт
    found = False
    count = 0
    with open(phone_book, "r", encoding="utf-8") as file:
        print("\n")
        for line in file:
            if name.lower() in line.lower():
                print(line)
                count += 1
                found = True
        if not found:
            print(f"Контакт {name} не найденю")
        if count > 1:
            print("\n")
            print(f"C именим {name} нашлись {count} контакта.")


def delete_contact(phone_book, name):  # удаляем контакт
    find_contact("address_book.txt", name)
    print('Для удаления введите полное имя контакта или введите "Отмена".')

    answer = input()

    if answer.lower() == "Отмена":
        main_menu()

    updated_lines = []
    contact_deleted = False

    with open(phone_book, "r", encoding="utf-8") as file:
        for line in file:
            if answer.lower() not in line.lower():
                updated_lines.append(line)
            else:
                contact_deleted = True

    if contact_deleted:
        with open(phone_book, "w", encoding="utf-8") as file:
            for line in updated_lines:
                file.write(line)
        print(f"Контакт {name} удален.")
    else:
        print(f"Контакт {name} не найден.")


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
            delete_contact("address_book.txt", name)
            # print("Контакт удален. ")
        elif choice == "3":
            name = input("Введите имя: ")
            find_contact("address_book.txt", name)
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

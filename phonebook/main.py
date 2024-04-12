from functions import add_contact, delete_contact, find_contact, show_all_contacts


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
            name = input("Введите имя: ")
            number = input("Введите номер телефона: ")
            add_contact(phone_book, name, number)
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

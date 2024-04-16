from functions import (
    add_contact,
    delete_contact,
    find_contact,
    show_all_contacts,
    ask_contact,
    copy_contact,
)


def main_menu():
    phone_book = {}
    while True:
        print("\n1. Добавить контакт")
        print("2. Удалить контакт")
        print("3. Найти контакт")
        print("4. Показать все контакты")
        print("5. Скопировать контакт")
        print("6. Выйти")
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
            # name = input("Введите имя: ")
            show_all_contacts("address_book.txt")
        elif choice == "5":
            print("Введите номер страки, которую нужно копировать:  ")
            contact_num = int(input())
            copy_contact("address_book.txt", contact_num)
        elif choice == "6":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")


if __name__ == "__main__":
    main_menu()

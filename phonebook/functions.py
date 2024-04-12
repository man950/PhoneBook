
def ask_contact(contacts):
    name = input("Введите имя: ")
    middle_name= input("Введите отчество: ")
    second_name = input("Введите фамилию: ")
    number = input("Введите номер телефона: ")
    contacts = {'Имя': name, 'Отсечтво': middle_name, 'Фамилия': second_name, 'Номер телефона': number }
    return contacts

def add_contact(phone_book, name, middle_name, second_name, number):
    ask_contact(contacts)
    print(f"Контакт {name} добавлен.")


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

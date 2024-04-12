
def add_contact(phone_book, name, number):
    phone_book[name] = number
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


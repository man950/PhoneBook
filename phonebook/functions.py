def ask_contact(contacts):  # спрашиваем данные контакта
    name = input("Введите имя: ")
    middle_name = input("Введите отчество: ")
    second_name = input("Введите фамилию: ")
    number = input("Введите номер телефона: ")
    notes = input("Заметки: ")
    contacts = {
        "Имя": name,
        "Отчество": middle_name,
        "Фамилия": second_name,
        "Номер телефона": number,
        "Заметки": notes,
    }

    print(f"Контакт {name} добавлен.", end="\n\n")
    return contacts


def add_contact(phone_book):  # добаляем контакт
    contact = ask_contact(phone_book)
    with open("address_book.txt", "a", encoding="utf-8") as file:
        for value in contact.values():
            file.write(str(value + "          "))
        file.write("\n")
    return True


def find_contact(phone_book, name):  # ишем еонтакт
    found = False
    count = 0
    print("\n")
    with open(phone_book, "r", encoding="utf-8") as file:
        print(" Имя", "Отчество", "Фанмлмя", "Номер", "Замерки", sep="          ")
        for idx, line in enumerate(file, start=1):
            if name.lower() in line.lower():
                print(idx, line)
                count += 1
                found = True
        if not found:
            print(f"Контакт {name} не найденю")
        if count > 1:
            # print("\n")
            print(f"C именим {name} нашлись {count} контакта.")


def delete_contact(phone_book, name):  # удаляем контакт
    find_contact("address_book.txt", name)
    print('Для удаления введите очередной номер контакта или введите "Отмена".')

    answer = input()
    if answer.lower() == "Отмена":
        main_menu()

    updated_lines = []
    contact_deleted = False
    with open(phone_book, "r", encoding="utf-8") as file:
        for idx, line in enumerate(file, start=1):
            if answer != str(idx):
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


def show_all_contacts(phone_book):  # показать все контакты
    with open(phone_book, "r", encoding="utf-8") as file:
        for idx, line in enumerate(file, start=1):
            print(f"{idx}. {line.strip()}")

        if file.tell() == 0:
            print("Телефонная книга пуста:")


def copy_contact(phone_book, num):  #
    with open(phone_book, "r", encoding="utf-8") as file:
        for idx, line in enumerate(file, start=1):
            if idx == num:
                with open("copied_contacts.txt", "w", encoding="utf-8") as file:
                    file.write(line)
                print("контакт скопирован")

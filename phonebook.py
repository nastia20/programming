contacts = {}

while True:
    command = input("Введіть команду (додати, видалити, пошук, показати, вихід): ").strip().lower()

    if command == "додати":
        name = input("Введіть ім'я: ")
        number = input("Введіть номер: ")
        contacts[name] = number
        print("Контакт додано!")

    elif command == "видалити":
        name = input("Введіть ім'я: ")
        if name in contacts:
            contacts.pop(name)
            print("Контакт видалено")
        else:
            print("Not found")

    elif command == "пошук":
        name = input("Введіть ім'я: ")
        number = contacts.get(name)
        if number:
            print(number)
        else:
            print("Not found")

    elif command == "показати":
        if len(contacts) == 0:
            print("Телефонна книга поки порожня.")
        else:
            for k, v in contacts.items():
                print(f"{k}: {v}")

    elif command == "вихід":
        print("Вихід з програми...")
        break

    else:
        print("Невідома команда")

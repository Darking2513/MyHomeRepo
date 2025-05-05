from homework4 import add_contact, change_contact, phone, show_all, parse_input

def main():
    contacts = {} # Словник для зберігання контактів

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip() # Отримуємо введення користувача
        if not user_input:
            continue # Якщо введення порожнє, пропускаємо ітерацію

        command, *args = parse_input(user_input) # Розділяємо введення на команду і аргументи
        command = command.lower() # Приводимо команду до нижнього регістру
        
        if command in ["close", "exit"]:# Завершення програми
            print("Good bye!")
            break

        elif command == "hello": # Привітання
            print("How can I help you?")

        elif command in ("add", "change", "phone"):
            
            if command == "add": # Додати контакт
                print(add_contact(args, contacts))
            elif command == "change": # Змінити номер телефону
                print(change_contact(args, contacts))
            elif command == "phone": # Показати номер телефону
                print(phone(args[0], contacts))

        elif command == 'all': # Показати всі контакти
            print(show_all(contacts))
            
        else: # Якщо команда не розпізнана
            print("Invalid command.")

if __name__ == "__main__":
    main()
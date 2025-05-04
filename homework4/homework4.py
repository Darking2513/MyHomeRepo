from typing import Callable

def input_error(func: Callable) -> Callable:
    # Функція-декоратор для обробки помилок введення
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Enter correct user name."
        except IndexError:
            return "Enter user name."
    return inner

@input_error
def add_contact(args, contacts):
    # Додати контакт
    name, phone = args
    if not phone.isdigit():
        raise ValueError("Phone number must contain only digits.")
    contacts[name] = phone
    return "Contact added."

def parse_input(user_input):
    # Тут розділи введення на команду і аргументи
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def change_contact(args, contacts: dict):
    # Зміни номер телефону
    name, new_phone = args
    if not new_phone.isdigit():
        raise ValueError("Phone number must contain only digits.")
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return "Contact not found."

@input_error
def phone(name, contacts: dict):
    # Показати номер телефону
    if name in contacts:
        return f"{name}: {contacts[name]}"
    else:
        return "Contact not found."

@input_error
def show_all(contacts: dict):
    # Виведи всі контакти
    if contacts:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts found.")
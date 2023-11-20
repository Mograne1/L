#Нещерет Максим
#ІКСМ-1
import os

def main():
    print("Ваш щоденник!")

    while True:
        choice = input("Виберіть опцію:\n1. Додати новий запис\n2. Переглянути всі записи\n3. Видалити запис\n4. Вийти\nВаш вибір: ")

        if choice == '1':
            add_entry()
        elif choice == '2':
            view_entries()
        elif choice == '3':
            delete_entry()
        elif choice == '4':
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте знову.")

def add_entry():
    entry = input("Введіть свій запис: ")

    with open('щоденник.txt', 'a') as file:
        file.write(entry + '\n')

    print("Запис успішно додано!")

def view_entries():
    if os.path.exists('щоденник.txt'):
        with open('щоденник.txt', 'r') as file:
            entries = file.readlines()
            if not entries:
                print("Щоденник порожній.")
            else:
                print("Ваші записи:")
                for i, entry in enumerate(entries, 1):
                    print(f"{i}. {entry.strip()}")
    else:
        print("Щоденник не знайдено.")

def delete_entry():
    view_entries()  
    entry_number = input("Введіть номер запису, який ви хочете видалити: ")

    try:
        entry_number = int(entry_number)
        with open('щоденник.txt', 'r') as file:
            entries = file.readlines()

        if 1 <= entry_number <= len(entries):
            deleted_entry = entries.pop(entry_number - 1)

            with open('щоденник.txt', 'w') as file:
                file.writelines(entries)

            print(f"Запис {entry_number} був видалений: {deleted_entry.strip()}")
        else:
            print("Невірний номер запису.")
    except ValueError:
        print("Введено некоректний номер запису.")

if __name__ == "__main__":
    main()

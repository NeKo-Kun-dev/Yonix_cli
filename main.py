import os
import sys
import shutil
from colorama import Fore, Style
import cowsay

COMMANDS = {
    "conf": "Выводит сведения о конфигурации компьютера",
    "wherei": "Выводит полный путь текущей директории",
    "chf": "Перейти в указанную директорию",
    "nf": "Создать новую директорию",
    "ef": "Удалить файл",
    "ed": "Удалить директорию",
    "rd": "Переименовать директорию",
    "ls": "Вывести список содержимого директории",
    "doc": "Вывести список команд",
    "exit": "Выйти из программы"
}

def print_banner():
    print(cowsay.daemon('Welcome to YoniX'))
    print(Fore.GREEN + 'Привет, добро пожаловать в новую мини CLI "YoniX"!' + Style.RESET_ALL)
    print('------------------------------------------------')
    print('Место для вашей рекламы')
    print('------------------------------------------------')
    print('С документацией можно ознакомиться введя команду "doc"')
    print('Нашел ошибку? Пиши: t.me/rashtarar')
    print('------------------------------------------------')
    print('Приступим!')
    print('------------------------------------------------')

def list_directory(path="."):
    try:
        files = os.listdir(path)
        print("\n".join(files) if files else "Папка пуста")
    except FileNotFoundError:
        print("Ошибка: Указанный путь не найден!")

def change_directory():
    dir_n = input("Введите путь к новой директории: ")
    if os.path.isdir(dir_n):
        os.chdir(dir_n)
    else:
        print("Ошибка: Директория не найдена!")

def create_directory():
    new_dir = input("Введите имя новой директории: ")
    try:
        os.mkdir(new_dir)
        print("Папка создана")
    except FileExistsError:
        print("Ошибка: Такая папка уже существует!")

def remove_file():
    rem_file = input("Введите имя файла для удаления: ")
    if os.path.isfile(rem_file):
        os.remove(rem_file)
        print("Файл успешно удален")
    else:
        print("Ошибка: Файл не найден!")

def remove_directory():
    rem_dir = input("Введите имя директории для удаления: ")
    if os.path.isdir(rem_dir):
        shutil.rmtree(rem_dir)
        print("Папка успешно удалена")
    else:
        print("Ошибка: Директория не найдена!")

def rename_directory():
    old_dir = input("Введите старое имя директории: ")
    new_name_dir = input("Введите новое имя директории: ")
    if os.path.isdir(old_dir):
        os.rename(old_dir, new_name_dir)
        print("Директория успешно переименована")
    else:
        print("Ошибка: Директория не найдена!")

def show_doc():
    print("Доступные команды:")
    for cmd, desc in COMMANDS.items():
        print(f"{cmd} - {desc}")

def main():
    print_banner()
    username = os.getlogin()
    
    while True:
        try:
            command = input(f"{Fore.YELLOW}{username} $ {Style.RESET_ALL}").strip()
            if not command:
                continue
            
            if command == "conf":
                print(os.environ)
            elif command == "wherei":
                print("Вы находитесь в " + os.getcwd())
            elif command == "chf":
                change_directory()
            elif command == "nf":
                create_directory()
            elif command == "ef":
                remove_file()
            elif command == "ed":
                remove_directory()
            elif command == "rd":
                rename_directory()
            elif command == "ls":
                path = input("Введите путь к директории (оставьте пустым для текущей): ").strip() or "."
                list_directory(path)
            elif command == "doc":
                show_doc()
            elif command == "exit":
                print("Goodbye!")
                sys.exit()
            else:
                print(Fore.RED + "Команда не распознана!" + Style.RESET_ALL)

        except KeyboardInterrupt:
            print("\nGoodbye!")
            sys.exit()
        except EOFError:
            print("\nGoodbye!")
            sys.exit()

if __name__ == "__main__":
    main()
# Функция для копирования строки из одного файла в другой
def copy_line(source_file, target_file, line_number):
    with open(source_file, 'r',encoding='utf-8') as f_source:
        lines = f_source.readlines()
        if line_number <= len(lines):
            with open(target_file, 'a') as f_target:
                f_target.write(lines[line_number - 1])
        else:
            print("Такой строки нет в файле")


# Ввод имени файла и числа строки для копирования
source_file = input("Укажите путь к  файлу со списком контактов: ")
target_file = input("Укажите путь к файлу, в который нужно скопировать контакт: ")
line_number = int(input("Введите номер строки для копирования: "))

# Вызов функции для копирования строки
copy_line(source_file, target_file, line_number)

print("Контакт успешно скопирован в другой файл.")

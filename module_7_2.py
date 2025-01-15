def custom_write(file_name, strings):
    strings_positions = {}


    with open (file_name, 'w', encoding='utf-8') as file:
        # Проходим по списку строк с их индексами, начиная с 1
        for index, string in enumerate(strings, start=1):
            # Получаем текущую позицию в байтах перед записью строки
            byte_position = file.tell()
            # Записываем строку в файл, добавляя символ новой строки ('\n')
            file.write(string + '\n')
            # Сохраняем информацию о позиции и строке в словарь
            strings_positions[(index, byte_position)] = string

    return strings_positions

# Пример использования функции

info = [
    'Text for tell.',  # Первая строка для записи
    'Используйте кодировку utf-8.',  # Вторая строка для записи
    'Because there are 2 languages!',  # Третья строка для записи
    'Спасибо!'  # Четвертая строка для записи
]
result = custom_write('test.txt', info)

for elem in result.items():

  print(elem)


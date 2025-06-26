# Из текстового файла (writer.txt) выбрать фамилии писателей, посчитать количество
# фамилий. Создать новый файл, в котором выполнить замену слова «роман» на слово
# «произведение».
import re

surname = r'^([\w\-]+)'

# Чтение файла
try:
    with open('C:/Users/lilia/OneDrive/Documents/GitHub/Python_Oru/PZ_14/writer.txt', 'r', encoding='utf-8') as file:
        text = file.read()
except FileNotFoundError:
    print("Ошибка: writer.txt не найден.")
    exit()

# Извлечение фамилий
all_surnames = set(re.findall(surname, text))
count_surnames = len(all_surnames)

print('Фамилии писателей:', all_surnames)
print('Количество фамилий:', count_surnames)

# Замена "роман" на "произведение"
new_words = text.replace('роман', 'произведение')

# Запись в новый файл
with open('C:/Users/lilia/OneDrive/Documents/GitHub/Python_Oru/PZ_14/writer1.txt', 'w', encoding='utf-8') as new_file:
    new_file.write(new_words)

print("Изменения записаны в writer1.txt") 
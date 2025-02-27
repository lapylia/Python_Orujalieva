# 1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Минимальный элемент:
# Числа кратные трем:
# Количество чисел кратных трем:

# Запишем в файл data_3.txt структуру данных - список
l = ['-99 6 12 -36 20 45 100 -15']
f3 = open('data_3.txt', 'w')
f3.writelines(l)
f3.close()

# Дублируем список в новый файл data_4.txt
f4 = open('data_4.txt', 'w', encoding="utf-8")
f4.write('Исходные данные: ')
f4.write('\n')
f4.writelines(l)
f4.close()

# разбиваем строку и ее значения преобразуем в числа
f3 = open('data_3.txt')
k = f3.read()
k = k.split()
for i in range(len(k)):
    k[i] = int(k[i])
f3.close()
# Ищем количество элементов, минимальный элемент, числа кратные трем, количество чисел кратных трем
# в файле data_3.txt и записываем в файл data_4.txt
f3 = open('data_3.txt')
count, min, count_digit_3 = 0, 0, 0
digit_3 = []
for i in range(len(k)):
    count += 1
    min = min if min < k[i] else k[i]
    if k[i] % 3 == 0:
        digit_3.append(k[i])
        count_digit_3 += 1

f4 = open('data_4.txt', 'a', encoding="utf-8") # открываем файл для дозаписи
f4.write('\n')
f4.write(f'Количество элементов: {count}\n')
f4.write(f'Минимальный элемент: {min}\n')
f4.write(f'Числа кратные трем: {digit_3}\n')
f4.write(f'Количество чисел кратных трем: {count_digit_3}\n')
f4.close()
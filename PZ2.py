# Ввод трехзначного числа
number = input("Введите трехзначное число: ")
while type(number) != int
    try: 
        number = int(number)
    except ValueError:
        print("Введено не целое число")
        number = input("Введите трехзначное число: ")
# Извлечение цифр
hundreds = number // 100          # Сотни
tens = (number // 10) % 10        # Десятки
units = number % 10                # Единицы

# Перестановка цифр и формирование нового числа
new_number = tens * 100 + hundreds * 10 + units

# Вывод результата
print("Новое число:", new_number)
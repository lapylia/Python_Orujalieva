# Даны два числа. Вывести вначале большее, а затем меньшее из них.
try:
    # Ввод двух чисел
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))

    # Сравнение чисел и вывод результата
    if a > b:
        print("Большее число:", a)
        print("Меньшее число:", b)
    else:
        print("Большее число:", b)
        print("Меньшее число:", a)

except ValueError:
    print("Ошибка: Пожалуйста, введите корректные числа.")
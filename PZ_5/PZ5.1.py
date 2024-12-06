#Дан прямоугольник,длины сторон которого равны натуральным числам А и В Составить функцию, которая будет находить на сколько квадратов можно разрезать данный прямоугольник, если от него каждый раз отрезать квадрат наибольшей площади.
def count_squares(A, B):
    # Проверка на положительность входных данных
    if A <= 0 or B <= 0:
        raise ValueError("Длины сторон A и B должны быть положительными числами.")

    count = 0
    while A > 0 and B > 0:
        count += 1
        if A > B:
            A -= B
        else:
            B -= A
    return count

# Пример использования функции
try:
    A = int(input("Введите длину стороны A: "))
    B = int(input("Введите длину стороны B: "))
    result = count_squares(A, B)
    print(f"Количество квадратов, на которые можно разрезать прямоугольник: {result}")
except ValueError as e:
    print(f"Ошибка: {e}")
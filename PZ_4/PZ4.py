#Дано вещественное число X и целое число N (> 0). Найти значение выражения 1 - X 2 /(2!) + X4 /(4!) - ... + (-1)N -X 2*N/((2-N)!) (N! = 12 ...N). Полученное число является приближенным значением функции cos в точке X.

def factorial(n):
    """Функция для вычисления факториала числа n."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def cosine_approximation(x, n):
    """Приближение числа косинуса с помощью ряда Тейлора."""
    result = 0
    for k in range(n + 1):
        # Вычисляем четные степени X
        term = ((-1) * k) * (x * (2 * k)) / factorial(2 * k)
        result += term
    return result

# Пример использования
X = float(input("Введите вещественное число X: "))
N = int(input("Введите целое число N (> 0): "))

if N > 0:
    cosine_value = cosine_approximation(X, N)
    print(f"Приближенное значение cos({X}) с помощью ряда Тейлора: {cosine_value}")
else:
    print("Ошибка: N должно быть больше 0.")
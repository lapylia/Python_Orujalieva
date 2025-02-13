#Дан целочисленный список размера N. Найти максимальное количество его одинаковых элементов
def max_equal_elements_count(arr):
    # Создаем словарь для подсчета количества вхождений элементов
    element_count = {}
    
    # Подсчитываем вхождения каждого элемента
    for num in arr:
        if num in element_count:
            element_count[num] += 1
        else:
            element_count[num] = 1
    
    # Находим максимальное количество одинаковых элементов
    max_count = max(element_count.values())
    
    return max_count

# Пример использования
try:
    N = int(input("Введите размер списка: "))
    if N <= 0:
        raise ValueError("Размер списка должен быть положительным числом.")
    
    arr = list(map(int, input("Введите элементы списка (через пробел): ").split()))
    
    if len(arr) != N:
        raise ValueError(f"Количество введённых элементов ({len(arr)}) не соответствует размеру списка ({N}).")
    
    result = max_equal_elements_count(arr)
    print("Максимальное количество одинаковых элементов:", result)

except ValueError as e:
    print(f"Ошибка: {e}")
except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")

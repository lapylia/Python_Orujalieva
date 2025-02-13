# Дан список размера N, все элементы которого, кроме одного, упорядочены по
#убыванию. Сделать список упорядоченным, переместив элемент, нарушающий
#упорядоченность, на новую позицию.
def reorder_list(lst):
    # Проверяем, является ли входной параметр списком
    if not isinstance(lst, list):
        raise TypeError("Входной параметр должен быть списком.")

    # Проверяем, содержит ли список сравнимые элементы
    for i in lst:
        if not isinstance(i, (int, float, str)):
            raise ValueError("Элементы списка должны быть сравнимыми (int, float, str).")

    n = len(lst)
    index_of_disorder = -1

    for i in range(1, n):
        if lst[i] > lst[i-1]:
            index_of_disorder = i
            break

    if index_of_disorder == -1:
        # Список уже упорядочен
        return lst

    # Элемент, который нарушает порядок
    disorder_element = lst[index_of_disorder]

    # Удаляем его из списка
    lst.pop(index_of_disorder)

    # Вставляем его на правильную позицию
    for i in range(n - 1):
        if lst[i] < disorder_element:
            lst.insert(i, disorder_element)
            return lst

    lst.append(disorder_element)  # Если элемент должен быть последним
    return lst

# Пример использования
try:
    N = 10
    my_list = [10, 8, 7, 6, 5, 4, 3, 9, 1, 0]  # Замените этот список, чтобы протестировать разные сценарии
    print(f"Исходный список: {my_list}")
    sorted_list = reorder_list(my_list)
    print(f"Упорядоченный список: {sorted_list}")
except TypeError as te:
    print(f"Ошибка: {te}")
except ValueError as ve:
    print(f"Ошибка: {ve}")

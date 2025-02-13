#Дан список размера N и целые числа К и L (1 < K < L < N ). Найти среднее арифметическое элементов список с номерами от К до L включительно.
def average_from_list(elements, K, L):
    if K < 1 or L > len(elements) or K > L:
        raise ValueError("Индексы K и L должны удовлетворять условиям: 1 <= K <= L <= N.")
    
    # Извлекаем подсписок элементов от K до L (включительно)
    subset = elements[K-1:L]  # K-1 и L, потому что индексы списков начинаются с 0
    average = sum(subset) / len(subset)
    
    return average

# Пример использования
N = 10  # Размер списка
elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Список из N элементов
K = 3
L = 7

try:
    result = average_from_list(elements, K, L)
    print(f"Среднее арифметическое элементов с номерами от до {L}: {result}")
except ValueError as e:
    print(e)
    
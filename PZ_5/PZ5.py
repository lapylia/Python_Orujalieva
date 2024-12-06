#Составить функцию, которая напечатает 40 любых элементов
import random
import string

def print_random_characters():
    try:
        # Генерируем 40 случайных символов из латинских букв и цифр
        characters = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=40))
        print(characters)
    except ValueError as e:
        print(f"Произошла ошибка: {e}")

print_random_characters()
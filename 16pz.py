#Создайте класс «Счетчик», который имеет атрибут текущего значения и методы для 
#инкремента и декремента значения
class Schethik:
    def __init__(self, nach_znachenie=0):
        self.tekyhee_znachenie = nach_znachenie

    def инкремент(self):
        self.tekyhee_znachenie += 1

    def декремент(self):
        self.tekyhee_znachenie -= 1

    def polytchit_znachenie(self):
        return self.tekyhee_znachenie


# Пример использования:
счётчик = Schethik(10)  # Начальное значение 10

Schethik.increment()
print(Schethik.polytchit_znachenie())  # Выведет 11

Schethik.decrement()
Schethik.decrement()
print(())  # Выведет 9

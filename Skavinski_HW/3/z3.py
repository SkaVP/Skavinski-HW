class NumbersList:
    def __init__(self, input_list):
        # Сохраняем только числовые элементы: int и float
        self.numbers = [x for x in input_list if isinstance(x, (int, float))]

    def show_list(self):
        # Метод для отображения содержимого списка
        print("Содержимое числового списка: ", self.numbers)

    def calculate_average(self):
        # Метод для вычисления среднего значения
        if not self.numbers:
            return None  # Возвращаем None, если список пуст
        return sum(self.numbers) / len(self.numbers)

list = [1, 'конь', 3.5, "keyboard", 48, 4, 9, "Питер", None, 7, '42', 0]
num_list = NumbersList(list)
print("Cодержимое начального списка: ", list)

num_list.show_list()
average = num_list.calculate_average()
print("Среднее значение: ", average)
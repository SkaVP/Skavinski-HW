class SortObject:
    def __init__(self, *args):
        texts = [arg for arg in args if isinstance(arg, str)]
        nums = [arg for arg in args if isinstance(arg, int)]

        # Объединение двух строк
        if len(texts) == 2 and len(nums) == 0:
            self.text = texts[0] + texts[1]

        # Сумма двух чисел
        elif len(nums) == 2 and len(texts) == 0:
            self.number = nums[0] + nums[1]


        # В остальных случаях — не создаются поля
        else:
            print("Некорректные аргументы для создания объекта.")

    def display(self):
        if hasattr(self, 'text'):
            print(f"Текст: {self.text}")
        if hasattr(self, 'number'):
            print(f"Число: {self.number}")
        if not hasattr(self, 'text') and not hasattr(self, 'number'):
            print("Условия не соблюдены.")

# Проверка функциональности
print("Объект 1:")
obj1 = SortObject("Привет", "Мир")
obj1.display()

print("\nОбъект 2:")
obj2 = SortObject(26, 48)
obj2.display()

print("\nОбъект 3:")
obj3 = SortObject("Текст", 42) # некорректный случай
obj3.display()

print("\nОбъект 4:")
obj4 = SortObject(5, "строка")  # некорректный случай
obj4.display()
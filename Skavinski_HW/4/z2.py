class Temperature:
    def __init__(self, celsius):
        self.__celsius = None  # временно, чтобы вызвать сеттер
        self.celsius = celsius  # используем сеттер для проверки

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Температура не может быть ниже -273.15°C (абсолютный ноль).")
        self.__celsius = value

    @property
    def fahrenheit(self):
        return self.__celsius * 9 / 5 + 32


# Пример использования
temp = Temperature(25)
print(temp.fahrenheit)  # 77.0

# Попытка установить недопустимую температуру
try:
    temp.celsius = -300
except ValueError as e:
    print("Ошибка:", e)
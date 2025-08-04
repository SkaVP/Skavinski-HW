class Vehicle:
    def __init__(self, max_speed, mileage):
        self._max_speed = max_speed          # защищённый атрибут
        self.__mileage = mileage             # приватный атрибут

    def display_info(self):
        print(f"Max Speed: {self._max_speed}, Mileage: {self.__mileage}")

    # Дополнительно: метод для доступа к приватному атрибуту, если нужно
    def get_mileage(self):
        return self.__mileage


class Bus(Vehicle):
    def __init__(self, max_speed, mileage, passenger_capacity):
        super().__init__(max_speed, mileage)
        self.passenger_capacity = passenger_capacity

    def display_info(self):
        # Доступ к приватному атрибуту через метод родителя
        mileage = self.get_mileage()
        print(f"Max Speed: {self._max_speed}, Mileage: {mileage}, Passenger Capacity: {self.passenger_capacity}")


# Пример использования
bus = Bus(180, 10000, 50)
bus.display_info()
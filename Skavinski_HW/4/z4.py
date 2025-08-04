class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary  # защищённый атрибут

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self._salary}")

    def set_salary(self, new_salary):
        if new_salary < 0:
            raise ValueError("Зарплата не может быть меньше 0.")
        self._salary = new_salary

    def get_salary(self):
        return self._salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self._salary}, Department: {self.department}")


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self._salary}, Language: {self.programming_language}")


# Пример использования
dev = Developer("Alice", 5000, "Python")
dev.display_info()

# Попытка установить отрицательную зарплату
try:
    dev.set_salary(-1000)
except ValueError as e:
    print("Ошибка:", e)
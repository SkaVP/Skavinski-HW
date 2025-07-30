class MyFirstClass:
    def __init__(self, a, b): #конструктор
        self.attr1 = a
        self.attr2 = b

    def show_attribute(self):
        print(f"Атррибут 1: {self.attr1}")
        print(f"Атрибут 2: {self.attr2}")

# создание объекта 
obj1 = MyFirstClass("Утро", 9)
obj2 = MyFirstClass("День", 12)
obj3 = MyFirstClass("Вечер", 18)
obj4 = MyFirstClass("Ночь", 00)

# Вызов атрибутов
obj1.show_attribute()
print("----")
obj2.show_attribute()
print("----")
obj3.show_attribute()
print("----")
obj4.show_attribute()
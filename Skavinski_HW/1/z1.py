a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

if a > b:
    a, b = b, a

result = sum(range(a, b + 1))

print("Сумма чисел от ", a, "до", b, "равна: ", result )
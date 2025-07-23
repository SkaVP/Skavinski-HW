numbers = []

while True:
    nums = input("Введите число (для завершения введите не числовой символ): ")
    try:
        num = float(nums) 
        numbers.append(num)
    except ValueError:
        break  

if numbers:
    print("Минимальное значение:", min(numbers))
    print("Максимальное значение:", max(numbers))
else:
    print("Вы не ввели ни одного числа.")

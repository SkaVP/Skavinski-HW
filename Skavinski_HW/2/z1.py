def encrypt_vowels(text):
    vowels = 'аеёиоуыэюя'
    shifted_vowels = 'еёиоуюяаэеи'
    
    result = ''
    for char in text:
        lower_char = char.lower()
        if lower_char in vowels:
            index = vowels.index(lower_char)
            new_char = shifted_vowels[index]
            # Сохраняем регистр
            result += new_char.upper() if char.isupper() else new_char
        else:
            result += char
    return result

user_input = input("Введите строку: ")
encrypted = encrypt_vowels(user_input)
print("Зашифрованная строка:", encrypted)
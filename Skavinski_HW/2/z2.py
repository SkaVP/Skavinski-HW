import string

# Ввод текста
text = input("Введите текст:\n")

# Удаление знаков препинания и приведение к нижнему регистру
translator = str.maketrans("", "", string.punctuation + "«»“”")
clean_text = text.translate(translator).lower()

# Получение списка слов
words = clean_text.split()

# Уникальные слова
unique_words = set(words)

# Самое длинное слово
longest_word = max(words, key=len) if words else ""

# Частота букв
letter_freq = {}
for char in clean_text:
    if char.isalpha():
        letter_freq[char] = letter_freq.get(char, 0) + 1

# Вывод
print(f"\nУникальных слов: {len(unique_words)}")
print(f"Самое длинное слово: \"{longest_word}\"")
print(f"Частота букв: {letter_freq}")
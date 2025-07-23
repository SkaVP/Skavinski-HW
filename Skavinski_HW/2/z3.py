data = [
    "  Иван Иванов  ", 
    "Петров;Петр ", 
    "Сидорова Анна ", 
    "  ОЛЕГ КУЗНЕЦОВ  ", 
    "МАРИЯ; ТРОФИМОВА"
]

def clean_name(s):
    # Убираем лишние пробелы, точки, точки с запятой
    s = s.strip().replace(';', ' ').replace('.', ' ')
    # Разделяем по пробелам и убираем пустые элементы
    parts = [p for p in s.split() if p]
    # Если сначала фамилия — переворачиваем
    if parts[0].istitle():  # "Имя Фамилия"
        name, surname = parts
    else:
        surname, name = parts
    # Приводим к формату: Имя Фамилия
    return f"{name.capitalize()} {surname.capitalize()}"

cleaned = [clean_name(entry) for entry in data]
print(cleaned)
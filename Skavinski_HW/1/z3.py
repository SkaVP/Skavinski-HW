students = [
    ("Иван", "Петров", [4, 5, 5, 4], [3, 4, 5, 3], 0.9),               # (Имя, Фамилия, [оценки по Python], [оценки по математике], посещаемость)
    ("Мария", "Иванова", [5, 5, 5, 5], [5, 5, 4, 5], 0.95),
    ("Алексей", "Сидоров", [3, 4, 3, 3], [4, 3, 4, 4], 0.7),
    ("Елена", "Козлова", [5, 4, 5, 5], [4, 5, 5, 5], 0.85),
    ("Дмитрий", "Смирнов", [2, 3, 2, 3], [3, 2, 2, 3], 0.5)
]

print("Студенты с низкой посещаемостью:") # проверка на посещаемость в 75%
for student in students:
    name, surname, python_grades, math_grades, visited = student
    if visited < 0.75:
        print(f"{name} {surname}")

best_student = None # лучший студент
best_avg = 0

for student in students:
    name, surname, python_grades, math_grades, _ = student
    total_grades = python_grades + math_grades
    avg = sum(total_grades) / len(total_grades)
    if avg > best_avg:
        best_avg = avg
        best_student = f"{name} {surname}"

print(f"\nЛучший студент: {best_student} (средний балл: {best_avg:.2f})")

for student in students: # кому нужно уделить больше внимания Python 
    name, surname, python_grades, math_grades, _ = student
    python_avg = sum(python_grades) / len(python_grades)
    math_avg = sum(math_grades) / len(math_grades)
    if python_avg < math_avg:
        print(f"\n{name} {surname} нужно уделить больше внимания Python!")
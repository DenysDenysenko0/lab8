students = {}

# Функція Денисенка Дениса для виведення інформації з словника
def print_teams(students):
    print("\nЖурнал:")
    for pib, data in sorted(students.items()):
        kyrs = data[0]
        grypa = data[1]
        s1 = data[2]
        s2 = data[3]
        s3 = data[4]
        s4 = data[5]
        print(f"{pib} - {grypa}, {kyrs} курс. Вища математика: {s1}, Дискретна математика: {s2}, Програмування: {s3}, Програмування мовою пайтон: {s4}")
    
    MenuQuestion()

# Функція Денисенка Дениса для додавання даних у словник
def add_team(students, pib):
    if pib in students:
        print(f"\nСтудент '{pib}' вже у журналі")
        answer = input("Бажаєте перезаписати дані?(Так/ні): ")
        if answer.lower() == "ні":
            print("Операцію скасовано.")
            MenuQuestion()
            return
    
    kyrs = input("Введіть курс студента: ")
    grypa = input("Введіть групу студента: ")
    s1 = input("Введіть оцінку за вищу математику: ")
    s2 = input("Введіть оцінку за дискретну математику: ")
    s3 = input("Введіть оцінку за програмування: ")
    s4 = input("Введіть оцінку за програмування на пайтон: ")

    students[pib] = [kyrs, grypa, s1, s2, s3, s4]

    print("Студента додано/оновлено.")
    MenuQuestion()

def MenuQuestion():
    answer = input("\nВийти у меню?(Так/ні, завершення роботи): ")
    if answer.lower() == "так":
        Menu()
    else:
        print("Завершення роботи.")

def Menu():
    print("\nМеню:")
    print("1 - Показати журнал")
    print("2 - Додати студента")
    print("0 - Завершення роботи")

    num = input("Оберіть пункт меню: ")

    if num == "1":
        print_teams(students)
    elif num == "2":
        pib = input("Введіть ПІБ студента (Прізвище_ім'я_побатькові): ")
        add_team(students, pib)
    elif num == "0":
        print("Завершення роботи.")
    else:
        print("\nНевірний вибір!\n")
        Menu()

Menu()
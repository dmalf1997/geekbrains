from sys import argv

task_1, hours, salary, bonus = argv

try:
    print(f"зарплата: = {int(hours) * int(salary) + int(bonus)}")
except ValueError:
    print("Введите только цифры")
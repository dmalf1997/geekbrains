a = input("Введите число a:")
a = float(a)
b = input("Введите число b:")
b = float(b)
i = 1

while a < b:
    a = a * 1.1
    i += 1

print(f"на {i}-й день спортсмен достиг результата — не менее {b} км.")
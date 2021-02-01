def sum(a,b):
    if b == 0:
        return exit("Нельзя делить на ноль")
    else:
        sum = a/b
        return sum

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

print(f"Результат деления: {sum(a,b)}")

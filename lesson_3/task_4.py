def my_func(x, y):
    stepen = x
    while y != -1:
        stepen = stepen * x
        y = y + 1
    return 1 / stepen


x = float(input("Введите число x: "))
y = int(input("Введите число y: "))

print(my_func(x, y))

a = []

def my_func(a,b,c):
    max_1 = sorted([a,b,c])[1]
    max_2 = sorted([a,b,c])[2]
    return print(max_1 + max_2)

for i in range(3):
    a.append(int(input("Введите число: ")))

my_func(a[0], a[1], a[2])


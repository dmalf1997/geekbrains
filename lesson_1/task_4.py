num = input("Введите число: ")
num = int(num)
num_max = 0

while num != 0:
    num_last = num % 10
    if num_max <= num_last:
        num_max = num_last
    num = num // 10

print(f"Самая большая цифра - {num_max}")
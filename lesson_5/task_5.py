from functools import reduce

def summator(prev_el, el):
    return int(prev_el) + int(el)

with open("task_5.txt", "w+") as file:
    file.write(input("Введите числа через пробел: "))
    file.seek(0)
    print(reduce(summator, file.read().split()))

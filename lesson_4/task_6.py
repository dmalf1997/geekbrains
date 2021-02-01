from itertools import count, cycle

iter_1 = int(input("до какого числа: "))

for el in count(7):
    if el > iter_1:
        break
    else:
        print(el)

print("-" * 100)

a = 0

for el in cycle(["privet", "menya", "zovut", "ne", "igor"]):
    if a > 20:
        break
    print(el)
    a += 1
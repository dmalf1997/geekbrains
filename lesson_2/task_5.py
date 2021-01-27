nabor = [7, 5, 3, 3, 2]
i = 0

elem = float(input("Введите натуральное число: "))

for i in range(0,len(nabor),1):
    if nabor[i] <= elem:
        nabor.insert(i + nabor.count(elem), elem)
        break
    if i == len(nabor) - 1:
        nabor.append(elem)
        break

print(nabor)
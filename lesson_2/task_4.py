stroka = input("Введите строку с пробелами").split(" ")
i = 1

for elem in stroka:
    if elem != "":
        print(f"{i} - {elem[:10]}")
        i+=1

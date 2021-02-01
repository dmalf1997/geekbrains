summa = 0
i = ""

def sum(stroka, summa):
    for x in stroka:
        if x != "":
            summa = summa + int(x)
            print(summa)
            print(x)
    return summa

while i != "?":
    stroka = input("Введите строку с пробелами").split(" ")
    i = stroka[-1]
    if stroka[-1] == "?":
        stroka.pop(-1)
    summa = sum(stroka, summa)
    print(f"сумма - {summa}")

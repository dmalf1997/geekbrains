spisok= []
elem = 0
while elem != "" and elem != "exit":
    elem = input("Введите элемент списка: ")
    spisok.append(elem)
    if elem == '' or elem == "exit":
        print("аларм! нельзя оставить список пустым")
        print("если бы я знал след урок, то сделал бы рекурсию или просто quit()")
        del spisok[-1]

print(spisok)

for k in range(1,len(spisok),2):
    spisok[k-1], spisok[k] = spisok[k], spisok[k-1]

print(spisok)
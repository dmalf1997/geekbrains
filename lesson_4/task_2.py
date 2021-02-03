spisok = input("Введите список чисел: ").split()

print([spisok[i] for i in range(1,len(spisok)) if int(spisok[i]) > int(spisok[i-1])])
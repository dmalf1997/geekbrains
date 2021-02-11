with open ("test.txt", "w") as file:
    while True:
        stroka = input("Введите строку: ")
        if stroka != "":
            file.write(f"{stroka}\n")
        else:
            break
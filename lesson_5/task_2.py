with open("test.txt", "r") as file:
    print(f"кол-во слов в строке: {[{num: len(line.split())} for num, line in enumerate(file, 1)]}")
    file.seek(0)
    print(f"кол-во строк в файле: {sum(1 for line in file)}")
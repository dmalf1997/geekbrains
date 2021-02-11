from functools import reduce

def summator(prev_el, el):
    return int(prev_el) + int(el)

with open("zp.txt", "r") as file:
    print([line[0: line.index(" ")] for line in file if int(line[line.index(" ") + 1: len(line)]) > 20000])
    file.seek(0)
    kolvo = sum(1 for line in file)
    file.seek(0)
    summa = int(reduce(summator, [line[line.index(' ') + 1: line.index('\n')] if line.find('\n') != -1 \
                                      else line[line.index(' ') + 1: len(line)] for line in file]))
    print(f"Средняя зп: {summa/kolvo:.2f}")
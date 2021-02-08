import re
from functools import reduce

def summator(prev_el, el):
    return int(prev_el) + int(el)


with open("task_6.txt", "r") as file:
    name = [elem[0:elem.find(":")] for elem in file]
    file.seek(0)
    massiv = [line[line.find(":")+1: len(line)].split() if line.find("—") == -1 \
            else line[line.find(":")+1: len(line)].split("—") for line in file]
    iteracia = {}
    i = 1
    for elem in massiv:
        iteracia.update({i: [re.sub('[^0-9]','', line) for line in elem]})
        iteracia[i] = [elem for elem in iteracia.get(i) if elem]
        i += 1

    itog = {}
    for i in range(1,4):
        itog.update({name[i-1]: reduce(summator, iteracia.get(i))})

    print(itog)
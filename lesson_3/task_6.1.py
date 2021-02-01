# это вариант 6 задачи, где я решил усложнить себе жизнь, ну и всякие штуки типо спец символов, но в задании такого нет

def int_func(letter):
    return letter.capitalize()


title = input("Введите слово: ").split()


for i in range (0,len(title),1):
    title[i] = int_func(title[i])

print(' '.join(title))
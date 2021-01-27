tovari = []
analytics = {"Название":[],"Цена": [], "кол-во":[], "ед":[]}
i = 1

while True:
    name = input("Введите название товара: ")
    price = float(input("Введите цену товара: "))
    quantity = float(input("Введите кол-во товара: "))
    measure = input("Введите ед измерения товара: ")
    tovari.append((i, {"Название": name, "Цена": price, "кол-во": quantity, "ед": measure}))
    i = i + 1
    prodoljit = input("Если хотите закончить вводить данные, напишите quit: ")
    if prodoljit == "quit":
        break

for k in range(0, len(tovari) - 1, 1):
    for key in analytics.keys():
        analytics[str(key)].append(tovari[k][1][str(key)])

print(analytics)
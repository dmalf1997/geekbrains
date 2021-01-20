revenue = input("Введите выручку фирмы: ")
revenue = float(revenue)
cost = input("Введите издержки фирмы: ")
cost = float(cost)

result = revenue - cost

if result > 0:
    print("Фирма отработала в прибыль")
    rate = result / revenue
    person = input("Сколько человек работает в фирме: ")
    person = int(person)
    result_person = result / person
    print(f"Рентабельность - {rate}, прибыль на одного сотрудника - {result_person}")
else:
    print("Фирма отработала в убыток")
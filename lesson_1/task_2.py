time_in = input("Введите время в секундах: ")
time_in = int(time_in)

time_h = time_in // 3600
time_m = (time_in % 3600) // 60
time_s = (time_in % 3600) % 60


if time_h < 10:
    time_h = "0" + str(time_h)
if time_m < 10:
    time_m = "0" + str(time_m)
if time_s < 10:
    time_s = "0" + str(time_s)

print(f"Время - {time_h}:{time_m}:{time_s}")
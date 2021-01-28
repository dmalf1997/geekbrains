

def user_data(name, surname, year, town, email, mobile):
    print(f"Имя: {name}, Фамилия: {surname}, Год рождения: {year}, Город: {town}, Почта: {email}, Телефон: {mobile}")

name = input("Введите имя: ")
surname = input("Введите фамилию: ")
year = input("Введите год рождения: ")
town = input("Введите город: ")
email = input("Введите почту: ")
mobile = input("Введите телефон: ")

user_data(name,surname,year,town,email,mobile)
seasons = {"zima": ["january", "december", "february"], "leto": ["june", "july", "august"], "vesna": ["march", "april", "may"], "osen": ["september", "october", "november"]}
months = {1: "january", 2: "february", 3: "march", 4: "april", 5: "may",6: "june", 7: "july", 8: "august", 9: "september", 10: "october", 11: "november", 12: "december"}

season_spisok = ["zima", "leto", "vesna", "osen"]

month_in = int(input("Введите номер месяца: "))
for season in season_spisok:
    for month in seasons.get(season):
        if month == months.get(month_in):
            print(f"ваш месяц: {month}, сезон: {season}")
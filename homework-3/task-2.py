import datetime
year = int(input("Enter birth year: "))
month = int(input("Enter birth month: "))
day = int(input("Enter birth day: "))

birth_day = datetime.date(year, month, day)
week_day = birth_day.weekday()

if week_day == 0:
	print("Week day of birthday is Monday")
elif week_day == 1:
	print("Week day of birthday is Tuesday")
elif week_day == 2:
	print("Week day of birthday is Wednesday")
elif week_day == 3:
	print("Week day of birthday is Thursday")
elif week_day == 4:
	print("Week day of birthday is Friday")
elif week_day == 5:
	print("Week day of birthday is Saturday")
else:
	print("Week day of birthday is Sunday")
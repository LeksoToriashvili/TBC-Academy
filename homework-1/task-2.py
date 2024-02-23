import datetime

name=input("Enter your FirstName: ")
birth_year=int(input("Enter your birth year: "))

current_year=datetime.date.today().year
age=current_year-birth_year
print("\nHello ", name, ", you are ", age, " years old.", sep="")
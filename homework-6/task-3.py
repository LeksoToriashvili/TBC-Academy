import random

comp_number = random.randint(1, 99)
number = 0
MAX_TRIES = 10
i = 1

while number != comp_number:
	number = int(input("Guess the number: "))
	if number > comp_number:
		print("high")
	elif number < comp_number:
		print("low")
	else:
		break
	if i >= MAX_TRIES:
		print("Computer is winner")
		break
	i += 1

if number == comp_number:
	print("You are winner")

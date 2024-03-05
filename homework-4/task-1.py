import random

number_of_players = int(input("Enter number of players: "))

if number_of_players<1:
	print("Number of players must be positive.")
else:
	for _ in range(number_of_players):
		print(random.randint(1, 6), random.randint(1, 6))

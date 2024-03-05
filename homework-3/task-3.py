import random

color = random.randint(0, 3)
card = str(random.randint(2, 14))

if card == "11":
	card = "J"
if card == "12":
	card = "Q"
if card == "13":
	card = "K"
if card == "14":
	card = "A"

if color == 0:
	color = "clubs"
elif color == 1:
	color = "diamonds"
elif color == 2:
	color = "hearts"
else:
	color = "spades"

print(f"The card is {card} of {color}")
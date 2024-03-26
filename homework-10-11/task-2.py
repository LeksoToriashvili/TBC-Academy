import random
import math

n = int(input("Enter number: "))

if n <=1:
	print("Entered number must be graeter than 1")
	exit(1)

counter = 0
for i in range(n):
	a=random.random()
	b=random.random()
	if math.sqrt(a ** 2 + b ** 2) <= 1:
		counter += 1

print(4 * counter / n)

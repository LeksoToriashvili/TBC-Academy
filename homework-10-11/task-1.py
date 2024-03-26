n = int(input("Enter number: "))

if n <=1:
	print("Entered number must be graeter than 1")
	exit(1)

x = 0
for i in range(n):
	x += ((-1) ** i) * (1 / (2 * i + 1))
print(x)

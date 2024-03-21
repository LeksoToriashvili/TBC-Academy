n = int(input("Enter number: "))

if n<1 or n > 1000:
	exit(1)

while n!=1:
	print(n, end = "->")
	if n % 2 == 0:
		n = int(n / 2)
	else:
		n = n * 3 + 1
print(n)

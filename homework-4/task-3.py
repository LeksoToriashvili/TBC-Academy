n = int(input("Enter number: "))

if n>0 and n<1000:
	for i in range(1, n):
		if n%i==0:
			print(f"{i} ", end="")
	print(n)
else:
	print("Enter number from (0, 1000) range.")

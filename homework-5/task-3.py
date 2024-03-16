n = int(input("Enter heightof christmas tree: "))

if n>0 and n<50:
	print(" " * (n - 1), "*")
	for i in range(1, n):
		print(" " * (n - i), end="")
		for j in range (n - i, n +i+1):
			if j>n:
				print("\\", end="")
			elif n>j:
				print("/", end="")
			else:
				print("|", end="")
		print()
	print(" " * (n - 1), "|")
else:
	print("Height must be in range (1...49)")

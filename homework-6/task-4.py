n = int(input("Enter number: "))

if n > 0 and n < 10:
	i = 1
	while i < 2 * n:
		j = 1
		if i < n:
			count = i + 1
		else:
			count = 2 * n - i + 1
		while j < count:
			print(j, end="")
			j += 1
		print()
		i += 1
else:
	print("Number must be from range (0, 10)")

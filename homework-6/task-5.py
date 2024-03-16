n = int(input("Enter number: "))

if n > 0 and n < 10:
	i = 0
	while i < n + 1:
		print(" " * 2 *(n - i), end = "")
		j = -i
		while j < i + 1:
			print(abs(j), "", end = "")
			j += 1
		print()
		i += 1
else:
	print("Number must be from range (0, 10)")

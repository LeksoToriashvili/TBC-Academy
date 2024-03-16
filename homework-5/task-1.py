n = int(input("Enter number: "))

if n>0 and n<50:
	for i in range(1, n+1):
		nprint = 0
		print(f"{i} - ", end="")
		for j in range(1, i+1):
			if i%j != 0:
				continue
			print(j, end=" ")
			nprint +=1
			if nprint == 3:
				break
		print()
else:
	print("Please enter number from range 1...49")

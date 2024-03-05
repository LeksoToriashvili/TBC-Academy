n = int(input("Enter index of fibonacci sequence: "))

a_1 = 1 #a(-1) is virtual member of sequence at index -1
a = 0 #a(0) is a first member of sequence

if n>=0 and n<20:
	for _ in range(n):
		a_1, a = a, a_1+a
	print(a)
else:
	print("Please enter number from [0, 20) range.")

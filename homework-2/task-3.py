a=int(input("Enter number: "))

if a>10:
	print("Number must be lower than 10")
elif a<0:
	print("Number must ne positive")
else:
	if a%2==0:
		print("2 ", end="")
	if a%3==0:
		print("3 ", end="")
	if a%5==0:
		print("5 ", end="")
	print()
n = int(input("Enter number: "))

if n < 0 or n > 9999:
	exit(1)

sum = 0
print("reversed number is ", end = "")
while n != 0:
	temp = n % 10
	print(temp, end = "")
	sum += temp
	n = n // 10
print("\nsum of digits:", sum)

def gcd_iter(a, b):
	while a % b != 0:
		a, b = b, a % b
	return b

def gcd_rec(a, b):
	if b == 0:
		return a
	return gcd_rec(b, a % b)

def main():
	a = int(input("Enter first number: "))
	b = int(input("Enter second number: "))
	
	if (a < 1 or a > 10000):
		print("number must be in range(0, 10000)")
		exit(-1)
	if (b < 1 or b > 10000):
		print("number must be in range(0, 10000)")
		exit(-1)
	
	print(f"GCD of {a} and {b} is {gcd_iter(a, b)}")

if __name__ == "__main__":
	main()

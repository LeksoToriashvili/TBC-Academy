import task_1

def lcm(a, b):
	return int(a * b / task_1.gcd_iter(a, b))

def main():
	a = int(input("Enter first number: "))
	b = int(input("Enter second number: "))
	
	if (a < 1 or a > 9999):
		print("number must be in range(0, 10000)")
		exit(-1)
	if (b < 1 or b > 9999):
		print("number must be in range(0, 10000)")
		exit(-1)
	
	print(f"LCM of {a} and {b} is {lcm(a, b)}")

if __name__ == "__main__":
	main()

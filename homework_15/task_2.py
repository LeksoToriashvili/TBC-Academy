def is_prime(a):
	if a < 1:
		return False
	for i in range(2, a):
		if a % i == 0:
			return False
	return True

def main():
	nums = [0, 1, 2, 3, 4, 5, 6]
	
	for i in nums:
		print (f"{i} is prime") if is_prime(i) else print (f"{i} is not prime")

if __name__ == "__main__":
	main()

import random

n = int(input("Enter number: "))
max = 0

if n>0 and n<30:
	for _ in range(n):
		rand_number = random.randint(0, 1000)
		#print(f"{rand_number} ", end="") #im shemtxvevashi tu generirebuli ricxvebis gamotana gvinda
		if max<rand_number:
			max = rand_number
	print(f"\n{max}")
else:
	print("Enter positive number.")

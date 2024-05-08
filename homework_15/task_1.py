import random

#function converts t temp to celsius if s = 'c' or fahrenheit if s = 'f'
def temp_convert(t, s):
	if s.lower() == "c":
		return (t - 32) * 5 / 9
	elif s.lower() == "f":
		return t * 9 / 5 + 32
	else:
		return -1

def main():
	t = random.randint(-100, 100)
	print(f"{t} celsius is {temp_convert(t, 'f')} fahrenheit")
	t = temp_convert(t, 'f')
	print(f"{t} fahrenheit is {temp_convert(t, 'c')} celsius")
	if t == temp_convert(temp_convert(t, "c"), "f"):
		print("It works!")

if __name__ == "__main__":
	main()

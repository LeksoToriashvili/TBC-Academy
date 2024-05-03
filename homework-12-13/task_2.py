import task_1

def check(text1, text2):
	res = False
	if len(text1) == len(text2):
		for _ in range(len(text1)):
			text2 = task_1.shift(text2)
			if text1 == text2:
				res = True
	return res

def main():
	text1 = input("Please enter text a: ")
	text2 = input("Please enter text b: ")
	print("Yes" if check(text1, text2) else "No")

if __name__ == "__main__":
	main()

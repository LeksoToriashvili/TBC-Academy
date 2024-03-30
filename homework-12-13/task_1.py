def shift(s):
	return s[-1]+s[:len(s)-1]

def main():
	text = input("Enter text: ")
	for _ in range(len(text)):
		text = shift(text)
		print(text)

if __name__ == "__main__":
	main()

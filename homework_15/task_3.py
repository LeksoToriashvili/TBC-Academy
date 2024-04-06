def reverse(text):
	if len(text) < 2:
		return text
	return reverse(text[1:]) + text[0]

def main():
	texts = ["Test", "Abc", "Python"]
	
	for t in texts:
		print(f"{t} -> {reverse(t)}")

if __name__ == "__main__":
	main()

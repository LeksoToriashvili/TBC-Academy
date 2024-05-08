def vowel_count(text):
	vowels = ['a', 'e', 'i', 'o', 'u']
	
	count = 0
	for c in text:
		if c.lower() in vowels:
			count += 1
	return count

def main():
	texts = ["Test", "Abc", "Kvaratskhelia"]
	
	for t in texts:
		print(f"{t} -> {vowel_count(t)}")

if __name__ == "__main__":
	main()

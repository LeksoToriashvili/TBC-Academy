word = input("Please input word: ")
chars = "AaEeIiOoUu"

for i in range(len(word)):
	if not(word[i] in chars):
		print(word[i], end = "")
print()

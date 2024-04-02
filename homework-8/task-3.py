word = input("Please input word: ")

if len(word) % 2 == 1:
	mid = word[int((len(word) - 1) / 2)]
else:
	mid = word[int(len(word) / 2) - 1] + word[int(len(word) / 2)]

i = 0
while i < 5:
	print(word[len(word) - 1], word[0], mid, sep = "", end = "")
	i += 1
print()

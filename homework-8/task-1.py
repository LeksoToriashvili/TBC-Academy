text = input("Please input text: ")

for i in range(len(text)):
	if i % 2 == 0 and text[i] != "e":
		print(text[i], end = "")
print()

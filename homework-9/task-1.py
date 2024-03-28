text = input("Enter text: ")
normal_text = ""

for c in text:
	if c.isalpha():
		normal_text = normal_text + c.lower()
reverse = normal_text[::-1]
print("Is palindrome" if normal_text == reverse else "Is not palindrome")

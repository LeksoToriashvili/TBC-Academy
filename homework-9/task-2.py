print("Enter texts:")
text1 = input()
text2 = input()

possible = False

if len(text1) == len(text2):
	for c in text1:
		index = text2.find(c)
		if index == -1:
			break
		else:
			text2 = text2.replace(c, "", 1)
	if len(text2) == 0:
		possible = True
print("YES" if possible else "No")

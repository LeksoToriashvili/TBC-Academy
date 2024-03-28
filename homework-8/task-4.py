row1 = "qwertyuiop"
row2 = "asdfghjkl"
row3 = "zxcvbnm"

action = input("Enter action (e/d): ")
if action != "e" and action != "d":
	print("Action is not valid...")
	exit(1)

text = input("Enter text: ")

if action == "e":
	increment = 1
else:
	increment = -1

for i in range (len(text)):
	if text[i] in row1:
		row = row1
	elif text[i] in row2:
		row = row2
	elif text[i] in row3:
		row = row3
	else:
		print(text[i], end = "")
		continue
	
	index = -1
	for j in range(len(row)):
		if text[i] == row[j]:
			index = j
			break
	index = (index + increment) % len(row)
	print(row[index], end = "")
print()

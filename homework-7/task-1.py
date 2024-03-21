n = int(input("Enter index of sequence: "))

if n<0 or n>19:
	exit(1)

last = 1 #virtual member of sequence at index=-1
current = 0 #first member of sequence at index=0

i = 0
while i < n:
	print(current, end=" ")
	last, current = current, last + current
	i += 1
print()

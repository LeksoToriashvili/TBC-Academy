speed=int(input("Enter speed of car: "))

if speed>120:
	print("Very fast")
elif speed>60:
	print("Fast")
elif speed>30:
	print("Moderate")
elif speed>0:
	print("Slow")
else:
	print("Speed must be positive number")
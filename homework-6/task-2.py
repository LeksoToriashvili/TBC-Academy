DB_PASSWORD = "Georgia"
MAX_TRIES = 3

input_password = input("Please enter password: ")

for i in range (MAX_TRIES):
	if input_password == DB_PASSWORD:
		print("Hello from Georgia")
		break
	if i == MAX_TRIES-1:
		print ("You are blocked!!!")
		break
	input_password = input("Password was not correct. Try again - ")

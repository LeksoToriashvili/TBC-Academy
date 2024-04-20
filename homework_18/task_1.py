def mean(t):
	s = 0
	for element in t:
		s += element
	return s / len(t)


def main():
	data = ((33, 34, 28), (24, 31, 27), (24, 23, 27), (28, 32, 34), (33, 21, 28), (20, 25, 31), (21, 31, 28))
	
	mean_week = 0
	print("Daily temperature report")
	for index, day in enumerate(data):
		print(f"Day {index+1}:")
	
		min_temp = min(day)
		max_temp = max(day)
		mean_temp = mean(day)
		mean_week += mean_temp
		
		print(f"Max = {max_temp}, Min = {min_temp}, Mean = {mean_temp}\n")
	
	mean_week /= len(data)
	print(f"Mean temperature of week is {mean_week}")


if __name__ == "__main__":
	main()

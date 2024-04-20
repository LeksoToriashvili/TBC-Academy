def midpoint(x1, y1, x2, y2):
	return (x1 + x2) / 2, (y1 + y2) / 2
	

def main():
	x1 = 1
	y1 = 2
	x2 = 3
	y2 = 4
	
	x, y = midpoint(x1, y1, x2, y2)
	print(f"Midpoint between startpoint ({x1}, {y1}) and endpoint ({x2}, {y2}) is ({x}, {y})")
	
	x2 = -1
	y2 = -2
	x, y = midpoint(x1, y1, x2, y2)
	print(f"Midpoint between startpoint ({x1}, {y1}) and endpoint ({x2}, {y2}) is ({x}, {y})")

if __name__ == "__main__":
	main()

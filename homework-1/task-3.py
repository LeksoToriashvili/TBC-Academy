import math

a=float(input("Enter first side of triangle: "))
b=float(input("Enter second side of triangle: "))
c=float(input("Enter third side of triangle: "))

#calculate semi perimeter
s=0.5*(a+b+c)

if s*(s-a)*(s-b)*(s-c)>0:
	#calculate area of triangle using Heron's formula
	a=math.sqrt(s*(s-a)*(s-b)*(s-c))
	
	print("\nPerimeter of the triangle is", 2*s)
	print("Area of the triangle is", a)
else:
	print("\nTriangle parameters is not valid")
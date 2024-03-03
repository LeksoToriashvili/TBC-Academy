import random
import math

start = float(input("Enter range start: "))
stop = float(input("Enter range stop: "))

rand = random.random()
new = abs(stop-start)*rand+start

print(new)


#using only random.random() function, write code to generate numbers from start to stop
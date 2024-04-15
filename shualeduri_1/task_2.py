n = int(input("Please enter number: "))

if n < 100 or n > 999:
    print("Entered number is wrong...")
    exit(-1)

count =0 
for i in range(1, n):
    if i % 13 == 0:
        print(i, " ", end="")
        count += 1

print(f"\nCount is {count}")

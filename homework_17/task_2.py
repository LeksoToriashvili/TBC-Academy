import random

def main():
    l1 = list()
    l2 = []
    l3 = list()

    for _ in range(10):
        l1.append(random.randrange(1, 10))
        l2.append(random.randrange(1, 10))
        l3.append(random.randrange(1, 10))
    
    sum = map(lambda x, y, z: x+y+z, l1, l2, l3)

    print(f"list1 - {l1}")
    print(f"list2 - {l2}")
    print(f"list3 - {l3}")
    print(f"Sum   - {list(sum)}")


if __name__ == "__main__":
    main()

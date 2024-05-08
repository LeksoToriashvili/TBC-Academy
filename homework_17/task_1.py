import random

def int_len(i):
    return len(str(i))

def main():
    my_list = list()
    for _ in range(100):
        my_list.append(random.randint(10, 1000000000))
    print(f"List - {my_list}") #temp
    _min = min(my_list, key = int_len)
    _max = max(my_list, key = int_len)
    print(f"\nMin - {_min}")
    print(f"\nMax - {_max}")
    sorted_list = sorted(my_list, key = int_len)
    print(f"\nSort ascending - {sorted_list}")
    sorted_list = sorted(my_list, key = int_len, reverse = True)
    print(f"\nSort descending - {sorted_list}")


if __name__ == "__main__":
    main()

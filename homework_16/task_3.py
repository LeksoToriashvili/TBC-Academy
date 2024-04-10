import random


def add_items(l, a):
    for _ in range(a):
        l.append(a)


def main():
    new_list = []
    random_numbers = []

    for _ in range(50):
        random_numbers.append(random.randint(1, 29))
    for number in random_numbers:
        if number not in new_list:
            new_list.append(number)

    print(f"List - {new_list}")
    print(f"Length - {len(new_list)}")


if __name__ == '__main__':
    main()

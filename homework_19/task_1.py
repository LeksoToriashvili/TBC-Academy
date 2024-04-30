import random


def is_even(n):
    return n % 2 == 0


def main():
    my_dict = {"even": 0, "odd": 0}
    for _ in range(100):
        if is_even(random.randint(0, 100)):
            my_dict["even"] += 1
        else:
            my_dict["odd"] += 1
    print(f"Even count is {my_dict['even']}")
    print(f"odd count is {my_dict['odd']}")


if __name__ == '__main__':
    main()

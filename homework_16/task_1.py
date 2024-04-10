def main():
    list = [22, 25, 19, 23, 25, 26, 23]

    sum = 0
    for item in list:
        sum += item
    mean = sum / len(list)

    print(mean)


if __name__ == "__main__":
    main()

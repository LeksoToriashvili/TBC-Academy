def main():
    my_dict = dict()
    text = input("Input some text: ")

    for c in text:
        if c in my_dict:
            my_dict[c] += 1
        else:
            my_dict[c] = 1
    for k, v in my_dict.items():
        print(f"{k} - {v}")


if __name__ == '__main__':
    main()

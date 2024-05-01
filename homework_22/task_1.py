#path of directory where the file is located. e.g. "/home/[username]/Documents/"
path = ""
filename = "data.txt"


def is_small(text):
    records = text.split(",")
    price = float(records[2]) * float(records[3])
    return price < 10


def main():
    file_small = open(path + "small.txt", 'w')
    file_high = open(path + "high.txt", 'w')

    with open(path + filename) as f:
        for line in f:
            if is_small(line):
                file_small.write(line)
            else:
                file_high.write(line)

    file_small.close()
    file_high.close()


if __name__ == "__main__":
    main()

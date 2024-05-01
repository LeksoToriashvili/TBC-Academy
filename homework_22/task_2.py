import json

#path of directory where the file is located. e.g. "/home/[username]/Documents/"
path = ""
filename = "data.txt"


def find_stats(data):
    res = {'a': [], 'b': [], 'c': 0, 'd': 0, 'e': []}

    max_product = (max(data, key=lambda x: int(x[2]))[2])
    for record in data:
        if record[2] == max_product:
            res['a'].append(record[0])

    d = dict()
    for record in data:
        if record[0] in d:
            d[record[0]] += record[4]
        else:
            d[record[0]] = record[4]
    max_paid = max(d.values())
    for key in d:
        if d[key] == max_paid:
            res["b"].append(key)

    mean = 0
    for record in data:
        mean += record[4]
    mean = mean / len(data)
    res["c"] = mean

    mean = 0
    for record in data:
        mean += record[2]
    mean = mean / len(data)
    res["d"] = mean

    d = dict()
    for record in data:
        if record[1] in d:
            d[record[1]] += record[3]
        else:
            d[record[1]] = record[3]
    max_product_count = max(d.values())
    for key in d:
        if d[key] == max_product_count:
            res["e"].append(key)

    return res


def main():
    data = list()
    with open(path + filename, "r") as f:
        for line in f:
            line = line.split(",")
            data.append([line[0], line[1], int(line[2]), float(line[3]), int(line[2]) * float(line[3])])

    with open(path + "stats.json", "w") as f:
        json.dump(find_stats(data), f, indent=4)


if __name__ == "__main__":
    main()

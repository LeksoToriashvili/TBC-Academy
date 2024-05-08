import json


def average_salary(data: dict) -> dict:
    res = dict()

    for key, value in data.items():
        try:
            sum = 0
            for k in value["employees"]:
                sum += int(k["salary"])
            avg = sum / len(value["employees"])
            res[value["name"]] = str(avg)
        except BaseException as err:
            res[value["name"]] = "Average salary for this department can't be calculated. Problem: "+str(err)

    return res


def readout(filename):
    with open(filename, 'r') as f:
        return json.load(f)


def main():
    filename = "data.json"

    try:
        data = readout(filename)
    except FileNotFoundError:
        print("File not found")
        exit(1)
    except BaseException:
        print("Something went wrong.")
        exit(2)

    avg_salary = average_salary(data)

    filename = "avg_salary.json"

    try:
        with open(filename, 'w') as f:
            json.dump(avg_salary, f, indent=4)
    except OSError as err:
        print("Something went wrong. Problem:", str(err))


if __name__ == "__main__":
    main()

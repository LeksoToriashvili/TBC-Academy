import json


def read_as_objects(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)

        departments = []
        for key, value in data.items():
            lis = []
            for emp in value["employees"]:
                lis.append(Employee(emp["name"], emp["position"], emp["salary"]))
            departments.append(Department(value["name"], value["description"], lis))
        return departments
    except FileNotFoundError:
        print('File not found')
    except Exception as e:
        print(e)


class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary


class Department:
    def __init__(self, name, description, employees):
        self.name = name
        self.description = description
        self.employees = employees

    def average(self):
        try:
            s = 0
            for employee in self.employees:
                s += int(employee.salary)
            s /= len(self.employees)
            return s
        except ValueError and ZeroDivisionError:
            print("Something went wrong")

    def max(self):
        try:
            return max(self.employees, key=lambda x: int(x.salary)).salary
        except ValueError:
            print("Something went wrong")

    def min(self):
        try:
            return min(self.employees, key=lambda x: int(x.salary)).salary
        except ValueError:
            print("Something went wrong")

    def positions(self):
        res = dict()
        for employee in self.employees:
            if employee.position in res:
                res[employee.position] += 1
            else:
                res[employee.position] = 1
        return res


def main():
    departments = read_as_objects("homework_1.json")

    for department in departments:
        print(F"Department Name: {department.name}")
        print(F"Department Description: {department.description}")
        print(F"Average salary: {department.average()}")
        print(F"Max salary: {department.max()}")
        print(F"Min salary: {department.min()}")
        print(F"Positions: {department.positions()}\n")


if __name__ == '__main__':
    main()

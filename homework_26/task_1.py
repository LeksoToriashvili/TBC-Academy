class Inset:
    def __init__(self):
        self._data = list()

    def __str__(self):
        try:
            self._data.sort()
        except Exception:
            print("Can't sort!")
        return str(self._data)

    @property
    def data(self):
        print("You cant access the data directly")
        return None

    @data.setter
    def data(self, data):
        print("Please use insert() method...")

    def insert(self, value):
        if value not in self._data:
            self._data.append(value)

    def member(self, value):
        if value in self._data:
            return True
        else:
            return False

    def remove(self, value):
        if value in self._data:
            self._data.remove(value)
        else:
            raise ValueError("Can't find value...")


def main():
    inset = Inset()

    inset.insert("python")
    inset.insert(2)
    inset.insert(3)
    inset.insert(1)

    if inset.member("python"):
        print("python is in inset")

    inset.remove("python")
    print(inset)
    inset.data = ["python"]
    print(inset.data)


if __name__ == '__main__':
    main()

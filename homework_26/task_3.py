class Extended(list):
    def __init__(self, arg):
        super().__init__(arg)

    def min(self):
        try:
            return min(self)
        except TypeError:
            print("Can't find minimal...")

    def max(self):
        try:
            return max(self)
        except TypeError:
            print("Can't find minimal...")


def main():
    e = Extended([1, 2, 3])
    ex = Extended([4, 5, 6, "asd"])
    print(e.min())
    print(e.max())
    print(ex.min())
    print(ex.max())


if __name__ == '__main__':
    main()

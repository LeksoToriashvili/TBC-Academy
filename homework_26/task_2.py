class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def insert(self, value):
        self.queue.append(value)

    def pop(self):
        if self.is_empty():
            raise ValueError('Queue is empty')

        return self.queue.pop(0)


def main():
    q = Queue()
    q.insert(1)
    q.insert("a")
    print(q.pop())
    q.insert(2.3)
    print(q.pop())
    print(q.pop())


if __name__ == '__main__':
    main()

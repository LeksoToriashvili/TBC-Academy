def merge(l1, l2):
    result = []
    if l1[-1] < l2[-1]:
        l1, l2, = l2, l1
    index1 = 0
    index2 = 0
    while len(l1) > index1:
        while index2 < len(l2) and l2[index2] < l1[index1]:
            result.append(l2[index2])
            index2 += 1
        result.append(l1[index1])
        index1 += 1
    return result


def main():
    list1 = [1, 3, 10]
    list2 = [0, 4, 7, 9]

    merged = merge(list1, list2)

    print(list1)
    print(list2)
    print()
    print(merged)


if __name__ == '__main__':
    main()

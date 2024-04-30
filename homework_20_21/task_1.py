import random
EXIT_KEYWORD = "finish"
CACHE_KEYWORD = "cache"
paths = {1: [1]}
iteration_count = 0


def calculate_series(n):
    global iteration_count

    result = [n]
    while n != 1:
        iteration_count += 1
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = 3 * n + 1
        result.append(n)
    return result


def calculate_series_cached(n):
    global iteration_count
    global paths
    orig = n
    result = []

    while True:
        if n in paths:
            paths[orig] = result + paths[n]
            return paths[orig]
        result.append(n)
        iteration_count += 1
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = 3 * n + 1


def main():
    global iteration_count
    while True:
        n = input("Please enter number or just hit enter for random number: ")
        if n == EXIT_KEYWORD:
            exit(0)
        elif n == CACHE_KEYWORD:
            print("Cache: ")
            for k in paths:
                print(f"{k} -> {paths[k]}")
            print("\n\n")
            continue
        elif n == "":
            n = random.randint(1, 50)
        else:
            n = int(n)

        print("---------------------------------------------------------------")
        print(f"calculating for n = {n}")

        iteration_count = 0
        res = calculate_series(n)
        print(f"{iteration_count} iterations using uncached function")
        print(res, "\n")

        iteration_count = 0
        res = calculate_series_cached(n)
        print(f"{iteration_count} iterations using cached function")
        print(res)

        print("\n\n")


if __name__ == '__main__':
    main()

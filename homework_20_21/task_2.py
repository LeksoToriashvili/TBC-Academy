EXIT_KEYWORD = "FINISH"
CACHE_KEYWORD = "CACHE"
graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['A', 'C']
}
cache = dict()


def exist(path, end_point):
    start_point = path[-1]
    if start_point in graph:
        if end_point in graph[start_point]:
            return True
        for item in graph[start_point]:
            if item in path:
                continue
            if exist(path + item, end_point):
                return True
    return False


def exist_cached(path, end_point):
    global cache
    start_point = path[-1]
    if start_point + end_point in cache:
        return cache[start_point + end_point]
    if start_point in graph:
        if end_point in graph[start_point]:
            return True
        for item in graph[start_point]:
            if item in path:
                continue
            if exist(path + item, end_point):
                cache[start_point + end_point] = True
                return True
    cache[start_point + end_point] = False
    return False


def main():
    while True:
        points = input("Please input start point and end point: ").replace(" ", "").upper()
        if points == EXIT_KEYWORD:
            exit(0)
        elif points == CACHE_KEYWORD:
            print(cache, "\n")
            continue
        elif len(points) < 2:
            exit(1)
        print(exist(points[0], points[1]), "\n")


if __name__ == '__main__':
    main()

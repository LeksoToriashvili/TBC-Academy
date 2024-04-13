def remove_elements(l):
    result = []
    for s in l:
        if not len(s) > 3:
            result.append(s)
    return result

def empty_elements(s):
    if len(s) > 3:
        return ""
    return s

def main():
    original_list = ["Python", "and", "or", "academy", "hydrogen"]
    print(original_list)

    map_list = list(map(empty_elements, original_list)) #using map function

    while("" in map_list):
        map_list.remove("")

    print(map_list)

    my_list = remove_elements(original_list) #using function

    print(my_list)


if __name__ == "__main__":
    main()

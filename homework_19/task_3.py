EXIT_KEYWORD = "FINISH"
SEPARATOR = "-"


def print_friendships(friendships):
    for k, v in friendships.items():
        print(f"{k} - ", end="")
        for person in v:
            print(person, end="")
            if person is not v[-1]:
                print("", end=", ")
        print()


def main():
    friendships = dict()

    while True:
        text = input("Enter friends names: ")
        if text == EXIT_KEYWORD:
            print("\nfriendships:")
            break
        if SEPARATOR not in text:
            print("Invalid input")
            exit(-1)
        person1, person2 = text.replace(" ", "").split("-")

        if person1 in friendships:
            if person2 not in friendships[person1]:
                friendships[person1].append(person2)
        else:
            friendships[person1] = [person2]

        if person2 in friendships:
            if person1 not in friendships[person2]:
                friendships[person2].append(person1)
        else:
            friendships[person2] = [person1]

    print_friendships(friendships)


if __name__ == '__main__':
    main()

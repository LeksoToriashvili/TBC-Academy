import random

def rand_generator():
    s = "RPS";
    i = random.randint(0, 2)
    return s[i]

def main():
    s = "RSP"
    user = input("Please enter R,P or S symbol: ")
    bot = rand_generator()

    print(f"Bot genrated {bot}")

    if bot == user:
        print("It's draw.")
        exit(0)

    user_index = s.index(user)
    if bot == s[user_index-1]:
        print("Computer win.")
    else:
        print("You win.")

if __name__ == "__main__":
    main()

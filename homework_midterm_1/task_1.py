import random


symbols = "RSP"


def winner(a, b):
    if a == b:
        return "Draw"
    if a == symbols[symbols.index(b) - 1]:
        return a
    else:
        return b


def rand_generator():
    return random.choice(symbols)


def main():
    user_score = 0
    bot_score = 0

    while user_score < 3 and bot_score < 3:
        user_choice = input("Please choose R(Rock), P(Paper) or S(Scissor): ").upper()

        if user_choice not in symbols:
            print(f'"{user_choice}" is not valid input...')
            return -1

        bot_choice = rand_generator()
        print(f"Computer chose {bot_choice}")

        if winner(user_choice, bot_choice) == user_choice:
            user_score += 1
            print("You won this round!")
        elif winner(bot_choice, user_choice) == bot_choice:
            bot_score += 1
            print("Computer won this round!")
        else:
            print("Draw!")

        print(f"User {user_score} : {bot_score} Computer\n")


if __name__ == '__main__':
    main()

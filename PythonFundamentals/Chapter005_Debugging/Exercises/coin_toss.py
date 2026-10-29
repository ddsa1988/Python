import random


def main() -> None:
    guess: str = ""
    coins = ("heads", "tails")

    while guess not in coins:
        print('Guess the coin toss! Enter heads or tails:')
        guess = input()

    toss: int = random.randint(0, 1)  # 0 is tails, 1 is heads

    if coins[toss] == guess:
        print('You got it!')
    else:
        print('Nope! Guess again!')
        guess = input()

        if coins[toss] == guess:
            print('You got it!')
        else:
            print('Nope. You are really bad at this game.')


if (__name__ == "__main__"):
    main()

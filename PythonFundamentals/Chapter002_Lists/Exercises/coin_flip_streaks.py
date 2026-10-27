import random


def generate_list_heads_and_tails(times: int) -> list[str]:
    if (type(times) != int or times < 1):
        return []

    COIN: list[str] = ["Heads", "Tails"]

    coin_flips: list[str] = []

    for _ in range(times):
        # random_index: int = random.randint(0, 1)
        # coin_flips.append(COIN[random_index])
        coin_flips.append(random.choice(COIN))

    return coin_flips


def get_number_streaks(coin_flips: list[str], streak: int) -> int:
    if (type(coin_flips) != list):
        TypeError("Coin flips must be a list type.")

    if (type(streak) != int or streak < 1):
        return 0

    list_heads: list[str] = ["Heads"] * streak
    list_tails: list[str] = ["Tails"] * streak

    number_streaks: int = 0

    for i in range(len(coin_flips)):
        list_slice: list[str] = coin_flips[i:i + streak]

        if (list_slice != list_heads and list_slice != list_tails):
            continue

        number_streaks += 1

    return number_streaks


def main() -> None:
    list_coin_flips: list[str] = generate_list_heads_and_tails(times=100)

    number_of_streaks: int = get_number_streaks(
        coin_flips=list_coin_flips, streak=6)

    print(list_coin_flips)
    print(number_of_streaks)


if (__name__ == "__main__"):
    main()

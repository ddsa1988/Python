def main() -> None:
    text: str = "Diego dos Santos Alexander"

    count_chars: dict[str, int] = {}

    for char in text:
        count_chars.setdefault(char, 0)
        count_chars[char] += 1

        # if (char in count_chars.keys()):
        #     count_chars[char] += 1
        # else:
        #     count_chars[char] = 1

    print(count_chars)


if (__name__ == "__main__"):
    main()

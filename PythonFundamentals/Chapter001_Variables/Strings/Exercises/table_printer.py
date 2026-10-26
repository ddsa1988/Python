def main():
    table_data: list[list[str]] = [["apples", "oranges", "cherries", "banana"], [
        "Alice", "Bob", "Carol", "David"], ["dogs", "cats", "moose", "goose"]]

    new_table_data: list[str] = []

    for row in table_data:
        longest_string: str = max(row, key=len)

        content: str = ""

        for i in range(len(row) - 1):
            content += row[i].rjust(len(longest_string)) + "\n"

        content += row[-1].rjust(len(longest_string))

        new_table_data.append(content)

    for item in new_table_data:
        print(item)
        print()


if (__name__ == "__main__"):
    main()

def main():
    cat: list[str] = ["fat", "gray", "loud"]

    size: str
    color: str
    disposition: str

    size, color, disposition = cat

    print(size)
    print(color)
    print(disposition)


if (__name__ == "__main__"):
    main()

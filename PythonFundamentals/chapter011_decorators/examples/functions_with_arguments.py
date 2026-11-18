from decorators import do_twice


@do_twice
def greet(name: str) -> None:
    print("Hello, " + name.strip().title() + ".")


def main() -> None:
    greet("diego")


if (__name__ == "__main__"):
    main()

def main() -> None:
    expected_output: str = "Hello World"
    test_1: str = "Hello World"
    test_2: str = "hello World"

    assert expected_output == test_1, "test_1 should be equal to expected_output"
    assert expected_output == test_2, "test_2 should be equal to expected_output"


if (__name__ == "__main__"):
    main()

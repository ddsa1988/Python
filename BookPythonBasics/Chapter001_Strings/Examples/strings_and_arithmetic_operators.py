def main()-> None:
    my_string:str = "2"
    my_number:int = 5

    print(f"{my_string} * {my_number} -> {my_string * my_number}")

    # try:
    #     print(f"{my_string} / {my_number} ->", end=" ")
    #     print(my_string / my_number)
    # except Exception as e:
    #     print(repr(e))

    # try:
    #     print(f"{my_string} - {my_number} ->", end=" ")
    #     print(my_string - my_number)
    # except Exception as e:
    #     print(repr(e))

    # try:
    #     print(f"{my_string} + {my_number} ->", end=" ")
    #     print(my_string + my_number)
    # except Exception as e:
    #     print(repr(e))


if(__name__ == "__main__"):
    main()
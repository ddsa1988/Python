def main()-> None:
    my_str_int_number:str = "10"
    my_str_float_number:str = "10.0"

    print(f"'{my_str_int_number}' to integer -> {int(my_str_int_number)}")
    print(f"'{my_str_float_number}' to float -> {float(my_str_float_number)}")

    try:
        print(f"'{my_str_int_number}' to float -> {float(my_str_int_number)}")
        print(f"'{my_str_float_number}' to integer ->", end=" ")
        print(int(my_str_float_number))
    except Exception as e:
        print(repr(e))


if(__name__ == "__main__"):
    main()
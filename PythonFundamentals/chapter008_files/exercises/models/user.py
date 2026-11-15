class User:
    def __init__(self, name: str, favorite_number: int) -> None:
        self.name = name
        self.favorite_number = favorite_number

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        if (type(name) != str):
            raise TypeError("name must be a string type.")

        if (len(name.strip()) == 0):
            raise ValueError("name can't be empty.")

        self._name = name.strip().lower()

    @property
    def favorite_number(self) -> int:
        return self._favorite_number

    @favorite_number.setter
    def favorite_number(self, number: int) -> None:
        if (type(number) != int):
            raise TypeError("number mus be an integer.")

        self._favorite_number = number

    def __str__(self) -> str:
        return f"User [name = {self.name}, favorite_number = {self.favorite_number}]"

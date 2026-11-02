class Car:
    class_variable: str = "Class attribute"

    def __init__(self, make: str, model: str, year: int) -> None:
        self.make = make
        self.model = model
        self.year = year

    def get_info_1(self) -> str:
        print(self)
        return f"Make = {self.make}, Model = {self.model}, Year = {self.year}"

    @classmethod
    def get_info_2(cls) -> str:
        print(cls)
        return cls.class_variable

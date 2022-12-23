from CustomExceptions.custom_exception import CustomException


class Multiplier:
    def __init__(self) -> None:  # constructor
        print("The result is shown below.")

    @staticmethod
    def calculate(x, y) -> int:  # self is needed always when the method can receive arguments
        if x.isdigit() and y.isdigit():
            x = int(x)
            y = int(y)
            if x < y:
                return x * y
            raise CustomException("The first number is greater than the second!")

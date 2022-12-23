from Multipliers.multiplier import Multiplier


def main():
    first_number = input("Type the first number:")
    second_number = input("Type the second number:")
    result = Multiplier()  # Instantiation
    print(result.calculate(first_number, second_number))


if __name__ == "__main__":
    main()

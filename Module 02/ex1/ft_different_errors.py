def garden_operations() -> tuple:
    print("Testing ValueError...")
    try:
        number = int("abc")
        return number
    except ValueError as error:
        print("Caught ValueError:", error, "\n")

    print("Testing ZeroDivisionError...")
    try:
        result = 10 / 0
        return result
    except ZeroDivisionError as error:
        print("Caught ZeroDivisionError:", error, "\n")

    print("Testing FileNotFoundError...")
    try:
        file = open("missing.txt", "r")
        file.close()
    except FileNotFoundError as error:
        print("Caught FileNotFoundError:", error, "\n")

    print("Testing KeyError...")
    try:
        plants = {"rose": 25}
        height = plants["missing_plant"]
        return height
    except KeyError as error:
        print("Caught KeyError:", error, "\n")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("Testing multiple errors together...")
    try:
        number = int("abc")
        result = 10 / 0
        return number, result
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!\n")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()

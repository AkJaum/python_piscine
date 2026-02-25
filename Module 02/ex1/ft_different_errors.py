def garden_operations():
    print("Testing ValueError...")
    try:
        number = int("abc")
    except ValueError as error:
        print("Caught ValueError:", error, "\n")

    print("Testing ZeroDivisionError...")
    try:
        result = 10 / 0
    except ZeroDivisionError as error:
        print("Caught ZeroDivisionError:", error, "\n")

    print("Testing FileNotFoundError...")
    try:
        file = open("missing.txt", "r")
    except FileNotFoundError as error:
        print("Caught FileNotFoundError:", error, "\n")

    print("Testing KeyError...")
    try:
        plants = {"rose": 25}
        height = plants["missing_plant"]
    except KeyError as error:
        print("Caught KeyError:", error, "\n")

def test_error_types():
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("Testing multiple errors together...")
    try:
        number = int("abc")
        result = 10 / 0
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!\n")

    print("All error types tested successfully!")

if __name__ == "__main__":
    test_error_types()

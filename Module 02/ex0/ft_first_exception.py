def check_temperature(temp_str):
    try:
        converted_str = int(temp_str)
        if (converted_str < 0):
            print("Error:", converted_str, "is too cold for plants (min 0°C)\n")
        elif (converted_str > 40):
            print("Error:", converted_str, "is too hot for plants (max 40°C)\n")
        else:
            print("Temperature", converted_str, "is perfect for plants!\n")
    except ValueError:
        print("Error: '", temp_str, "' is not a valid number\n", sep="")

def test_temperature_input():
    print("=== Garden Temperature Checker ===\n")
    testes = ["25", "abc", "100", "-50"]
    for teste in testes:
        print("Testing temperature:", teste)
        check_temperature(teste)
    print("All tests completed - program didn't crash!")

if __name__ == "__main__":
    test_temperature_input()

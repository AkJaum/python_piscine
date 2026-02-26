class GardenError(Exception):
    def __init__(self, message="GardenError") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="PlantError") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="WaterError") -> None:
        super().__init__(message)


def test_plant_error(last_watering: int) -> None:
    if last_watering > 2:
        raise PlantError("Plants neeed water!")
    elif last_watering < 0:
        raise PlantError("Invalid value, must be > 0")
    print("Plants are fine.\n")


def test_water_error(temp: int) -> None:
    if temp < 0 or temp > 40:
        raise WaterError("Water temperature must be between 0 and 40 degrees.")
    print("Water temperature is valid:", temp, "°C\n")


def test_custom_errors():
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError")
    try:
        test_plant_error(-1)
    except PlantError as Error:
        print("Caught PlantError:", Error, "\n")
    print("Testing WaterError")
    try:
        test_water_error(-5)
    except WaterError as Error:
        print("Caught WaterError:", Error, "\n")
    print("Testing catching all garden errors...")
    try:
        test_plant_error(3)
    except GardenError as e:
        print("Caught a garden error:", e)
    try:
        test_water_error(41)
    except GardenError as e:
        print("Caught a garden error:", e)
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()

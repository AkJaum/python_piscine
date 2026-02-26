class PlantError(Exception):
    def __init__(self, message="PlantError") -> None:
        super().__init__(message)


def check_plant_health(
    plant_name: str, water_level: int, sunlight_hours: int
) -> None:
    try:
        if plant_name == "" or plant_name is None:
            raise PlantError("Plant name cannot be empty!")
        elif water_level > 10:
            raise PlantError(
                f"Water level {water_level} is too high (max 10)"
                )
        elif water_level < 1:
            raise PlantError(
                f"Water level {water_level} is too low (min 1)"
            )
        elif sunlight_hours > 12:
            raise PlantError(
                f"Sunlight hours {sunlight_hours} is too high (max 12)"
            )
        elif sunlight_hours < 2:
            raise PlantError(
                f"Sunlight hours {sunlight_hours} is too low (min 2)"
            )
        else:
            print("Plant '", plant_name, "' is healthy!\n", sep="")
    except PlantError as Error:
        print("Error:", Error, "\n")


def test_plant_checks():
    print("=== Garden Plant Health Checker ===\n")
    print("Testing with good values...")
    check_plant_health("tomato", 8, 8)
    print("Testing empty plant name...")
    check_plant_health("", 8, 8)
    print("Testing bad water level...")
    check_plant_health("tomato", 0, 8)
    print("Testing bad sunlight hours...")
    check_plant_health("tomato", 8, 1)
    print("All errors raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()

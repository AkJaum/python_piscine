class GardenError(Exception):
    def __init__(self, message="GardenError"):
        super().__init__(message)

class PlantError(GardenError):
    def __init__(self, message="PlantError"):
        super().__init__(message)

def water_plants(plant_list):
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise PlantError("Cannot water None - invalid plant!")
            if not isinstance(plant, str):
                raise PlantError("Invalid plant type!")
            if plant == "":
                raise PlantError("Plant name cannot be empty!")
            print("Watering", plant)
    except PlantError as Error:
        print("Error:", Error)
    finally:
        print("Closing watering system (cleanup)")

def test_watering_system():
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    try:
        water_plants(["tomato", "lettuce", "carrots"])
        print("Watering completed succesfully!\n")
    except GardenError:
        print("Unexpected garden error!")
    print("Testing with error...")
    try:
        water_plants(["tomato", None, "carrots"])
    finally:
        print("\nCleanup always happens, even with errors!")

if __name__ == "__main__":
    test_watering_system()

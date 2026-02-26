class GardenError(Exception):
    def __init__(self, message="GardenError") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="PlantError") -> None:
        super().__init__(message)


class Planta():
    def __init__(
        self, name: str, water_level: int, sunlight_hours: int
    ) -> None:
        self.name = name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours


class GardenManager():
    def __init__(self):
        self.plants = []

    def create_plant(
        self, name: str, water_level: int, sunlight_hours: int
    ) -> None:
        try:
            if not name:
                raise PlantError("Plant name cannot be empty!")
            plant = Planta(name, water_level, sunlight_hours)
            self.plants.append(plant)
            print("Added", name, "successfully")
            return plant
        except PlantError as Error:
            print("Error adding plant:", Error)

    def water_plants(self, plants: list) -> None:
        try:
            print("Opening watering system")
            for plant in plants:
                if plant.name is None or plant.name == "":
                    print("Cannot water None - invalid plant!")
                if not isinstance(plant.name, str):
                    raise PlantError("Invalid plant type!")
                print("Watering", plant.name, "- success")
        except PlantError as Error:
            print("Error watering plant:", Error)
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plants: list) -> None:
        try:
            for plant in plants:
                if plant.name == "" or plant.name is None:
                    raise PlantError("Plant name cannot be empty!")
                elif plant.water_level > 10:
                    raise PlantError(
                        f"{plant.name}: Water level "
                        f"{plant.water_level} is too high (max 10)"
                    )
                elif plant.water_level < 1:
                    raise PlantError(
                        f"{plant.name}: Water level "
                        f"{plant.water_level} is too low (min 1)"
                    )
                elif plant.sunlight_hours > 12:
                    raise PlantError(
                        f"{plant.name}: Sunlight hours "
                        f"{plant.sunlight_hours} is too high (max 12)"
                    )
                elif plant.sunlight_hours < 2:
                    raise PlantError(
                        f"{plant.name}: Sunlight hours "
                        f"{plant.sunlight_hours} is too low (min 2)"
                    )
                else:
                    print(
                        f"{plant.name}: healthy (water: "
                        f"{plant.water_level}, sun: {plant.sunlight_hours})"
                    )
        except PlantError as Error:
            print("Error checking", Error)

    def error_recovery(self, water_level: int) -> None:
        try:
            if water_level < 20:
                raise PlantError("Not enough water in tank")
            else:
                print("Water tank is fine!")
        except GardenError as Error:
            print("Caught GardenError:", Error)
        finally:
            print("System recovered and continuing...")


def test_garden_management():
    manager = GardenManager()
    print("=== Garden Management System ===")
    print("\nAdding plants to garden...")
    manager.create_plant("tomato", 5, 8)
    manager.create_plant("lettuce", 15, 8)
    manager.create_plant("", 15, 8)
    print("\nWatering plants...")
    manager.water_plants(manager.plants)
    print("\nChecking plant health...")
    manager.check_plant_health(manager.plants)
    print("\nTesting error recovery...")
    manager.error_recovery(10)
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()

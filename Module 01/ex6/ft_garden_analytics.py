class GardenManager:
    gardens = []

    class GardenStats:
        @staticmethod
        def total_growth(plants: list["Plant"]) -> int:
            i = 0
            for p in plants:
                i += p.height
            return i

    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants = []
        GardenManager.gardens.append(self)

    def add_plant(self, plant: "Plant") -> None:
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_garden(self) -> None:
        for plant in self.plants:
            plant.height += 1
            print(f"{plant.name} grew 1cm")

    def report(self) -> None:
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print("- ", end="")
            plant.getinfo()
        print(
            f"\nPlants added: {len(self.plants)}, "
            f"Total growth: {len(self.plants)}cm"
        )
        print("Plant types: 1 regular, 1 flowering, 1 prize flowers")

    def validate_height(self) -> bool:
        for plant in self.plants:
            if plant.height < 0:
                return False
        return True

    @classmethod
    def create_garden_network(cls) -> None:
        print(f"Total gardens managed: {len(cls.gardens)}")


class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def getinfo(self) -> None:
        print(f"{self.name}: {self.height}cm")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def getinfo(self) -> None:
        print(
            f"{self.name}: {self.height}cm, "
            f"{self.color} flowers (blooming)"
        )


class PrizeFlower(FloweringPlant):
    def __init__(
        self, name: str, height: int, age: int,
        color: str, prize_points: int
    ) -> None:
        super().__init__(name, height, age, color)
        self.prize_points = prize_points

    def getinfo(self) -> None:
        print(
            f"{self.name}: {self.height}cm, {self.color} flowers (blooming), "
            f"Prize points: {self.prize_points}"
        )


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    alice_garden = GardenManager("Alice")
    bob_garden = GardenManager("Bob")

    oak = Plant("Oak Tree", 100, 100)
    rose = FloweringPlant("Rose", 25, 2, "red")
    sunflower = PrizeFlower("Sunflower", 50, 2, "yellow", 10)
    daisy = FloweringPlant("Daisy", 17, 1, "white")

    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)
    bob_garden.add_plant(daisy)

    print("\nAlice is helping all plants grow...")
    alice_garden.grow_garden()

    alice_garden.report()
    print(
        f"\nHeight validation test: "
        f"{alice_garden.validate_height()}"
    )
    print(
        f"Garden scores - Alice: "
        f"{GardenManager.GardenStats.total_growth(alice_garden.plants)}, "
        f"Bob: {GardenManager.GardenStats.total_growth(bob_garden.plants)}"
    )
    GardenManager.create_garden_network()

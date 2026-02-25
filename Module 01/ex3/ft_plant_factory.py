class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        print(
            "Created: ", self.name, " (", self.height,
            "cm ", self.age, " days)", sep=""
        )


def ft_plant_factory():
    plants_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]
    plants = []
    print("=== Plant Factory Output ===")
    for i in range(len(plants_data)):
        name = plants_data[i][0]
        height = plants_data[i][1]
        age = plants_data[i][2]
        plant = Plant(name, height, age)
        plants.append(plant)
    print("\nTotal plants created:", len(plants))


if __name__ == "__main__":
    ft_plant_factory()

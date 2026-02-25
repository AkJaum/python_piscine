class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")

    rose = Plant("Rose", "25cm", 30)
    sunflower = Plant("Sunflower", "80cm", 45)
    cactus = Plant("Cactus", "15cm", 120)

    print(f"{rose.name}: {rose.height}, {rose.age} days old")
    print(f"{sunflower.name}: {sunflower.height}, {sunflower.age} days old")
    print(f"{cactus.name}: {cactus.height}, {cactus.age} days old")

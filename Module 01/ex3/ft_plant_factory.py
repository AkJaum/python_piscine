class Planta:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def creation_log(self):   
        print("Created: ", self.name, " (", self.height, "cm ", self.age, " days)", sep = "")

if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    rose = Planta("Rose", 25, 30)
    oak = Planta("Oak", 200, 365)
    cactus = Planta("Cactus", 5, 90)
    sunflower = Planta("Sunflower", 80, 45)
    fern = Planta("Fern", 15, 120)
    rose.creation_log()
    oak.creation_log()
    cactus.creation_log()
    sunflower.creation_log()
    fern.creation_log()
    print("\nTotal plants created: 5")

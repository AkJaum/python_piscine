class Planta:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    rose = Planta("Rose", "25cm", 30)
    sunflower = Planta("Sunflower", "80cm", 45)
    cactus = Planta("Cactus", "15cm", 120)
    print(rose.name,": ", rose.height, ", ", rose.age, " days old", sep="")
    print(sunflower.name,": ", sunflower.height, ", ", sunflower.age, " days old", sep="")
    print(cactus.name,": ", cactus.height, ", ", cactus.age, " days old", sep="")

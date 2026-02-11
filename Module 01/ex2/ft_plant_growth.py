class Planta:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    def grow(self):
        self.height += 1

    def age_one_day(self):
        self.age += 1

    def get_info(self):
        print(self.name, ": ", self.height, "cm, ", self.age, " days old", sep = "")

if __name__ == "__main__":
    i = int(0)

    rose = Planta("Rose", 25, 30)
    print("=== Day 1 ===")
    rose.get_info()
    while (i < 6):
        rose.grow()
        rose.age_one_day()
        i += 1
    print("=== Day 7 ===")
    rose.get_info()
    print("Growth this week: +", i,"cm", sep = "")

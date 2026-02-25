class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def basic_info(self):
        return self.name, self.height, self.age


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(self.name, "is blooming beautifully!\n")

    def display(self):
        print(self.name, " (Flower): ",
              self.height, "cm, ",
              self.age, " days, ",
              self.color, " color", sep="")
        self.bloom()


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        shade_area = self.height // 2
        print(self.name, "provides", shade_area, "square meters of shade\n")

    def display(self):
        print(self.name, " (Tree): ",
              self.height, "cm, ",
              self.age, "days, ",
              self.trunk_diameter, " cm diameter", sep="")
        self.produce_shade()


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def display(self):
        print(self.name, " (Vegetable): ",
              self.height, "cm, ",
              self.age, " days, ",
              self.harvest_season, " harvest", sep="")
        self.nutrition_info()

    def nutrition_info(self):
        print(self.name, "is rich in",
              self.nutritional_value)


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")

    rose = Flower("Rose", 25, 30, "red")
    oak = Tree("Oak", 500, 1825, 50)
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")

    plants = [rose, oak, tomato]

    for plant in plants:
        plant.display()

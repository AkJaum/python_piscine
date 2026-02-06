class Planta:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

def ft_age():
    rose.height += 1
    rose.age += 1
    cactus.height += 1
    cactus.age += 1

def ft_get_info(day):
    print("=== Day", day, "===")
    print(rose.name, ": ", rose.height, "cm, ", rose.age, " days old", sep = "")
    print(cactus.name, ": ", cactus.height, "cm, ", cactus.age, " days old", sep = "")
    if (day == 7):
        print("Groth this week: +", day - 1, "cm", sep = "")

if __name__ == "__main__":
    i = int(1)
    rose = Planta("Rose", 25, 30)
    cactus = Planta("Cactus", 12, 18)
    ft_get_info(i)
    while (i < 7):
        ft_age()
        i += 1
    ft_get_info(i)

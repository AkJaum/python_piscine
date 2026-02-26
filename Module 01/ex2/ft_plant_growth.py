class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        self.height += 1

    def age_one_day(self) -> None:
        self.age += 1

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    rose.get_info()
    for _ in range(6):
        rose.grow()
        rose.age_one_day()
    print("=== Day 7 ===")
    rose.get_info()
    print("Growth this week: +", 6, "cm", sep="")

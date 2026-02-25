class SecurePlant:
    def __init__(self, name, height, age):
        self._name = name
        self._height = 0
        self._age = 0

        if height < 0:
            print("Security: Negative height rejected")
        else:
            self._height = height

        if age < 0:
            print("Security: Negative age rejected")
        else:
            self._age = age

        print("Plant created:", self._name)

    def set_height(self, new_height):
        if new_height < 0:
            print("\nInvalid operation attempted: height ",
                  new_height, "cm [REJECTED]", sep="")
            print("Security: Negative height rejected")
            return
        self._height = new_height
        print("Height updated: ", self._height, "cm [OK]", sep="")

    def set_age(self, new_age):
        if new_age < 0:
            print("\nInvalid operation attempted: age ",
                  new_age, "days [REJECTED]", sep="")
            print("Security: Negative age rejected")
            return
        self._age = new_age
        print("Age updated:", self._age, "days [OK]")

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def get_name(self):
        return self._name


if __name__ == "__main__":
    print("=== Garden Security System ===")

    rose = SecurePlant("Rose", 28, 30)

    rose.set_height(25)
    rose.set_age(30)
    rose.set_height(-5)

    print("\nCurrent plant: ",
          rose.get_name(),
          " (",
          rose.get_height(),
          "cm, ",
          rose.get_age(),
          " days)", sep="")

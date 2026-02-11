class SecurePlant:
    def __init__(self, name, height, age):
        if (height < 0):
            print("Security: Negative height rejected")
            return;
        if (age < 0):
            print("Security: Negative age rejected")
            return;
        self._name = name
        self._height = height
        self._age = age
        print("Plant created:", name)
    
    def set_height(new_height, self):
        if (new_height < 0):
            print("Invalid operation attempted: height ", new_height, "cm [REJECTED]", sep="")
            print("Security: Negative height rejected")
            return;
        self.height = new_height
        print("Height updated: ", self.height,"cm [OK]", sep="")

    def sef_age(new_age, self):
        if (new_age < 0):
            print("\nInvalid operation attempted: age", new_age, "[REJECTED]")
            print("Security: Negative age rejected")
        print("Age updated:", new_age, "days [OK]")

    def get_height(self):
        return (self.height)

    def get_age(self):
        return (self.age)

if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 25, 30)
    rose.set_height(25)
    rose.set_age(31)
    rose.set_height(-5)
    print(f"\nCurrent plant: {rose.name}")

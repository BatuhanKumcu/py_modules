class Plant:
    def __init__(self, name: str, height: float, day_old: int) -> None:
        self.name = name
        self.height = height
        self.day_old = day_old

    def get_height(self) -> float:
        return self.height

    def get_age(self):
        return self.day_old

    def set_height(self, new_height: float) -> None:
        if new_height >= 0:
            self.height = new_height
            print(f"Height updated: {new_height} cm")
        else:
            print(f"{self.name}: Error, height cant be negative")
            print("Height update rejected")

    def set_age(self, new_age: float) -> None:
        if new_age >= 0:
            self.day_old = new_age
            print(f"Age updated: {new_age} cm")
        else:
            print(f"{self.name}: Error, age cant be negative")
            print("Age update rejected")

    def growth(self, growing_rate: float) -> None:
        self.height = self.height + growing_rate

    def age(self, plus_day: int=1) -> None:
        self.day_old += plus_day

    def show(self) -> None:
        print(f"{self.name}: {round(self.height,1)}cm, {self.day_old} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.2, 8)
    rose.show()
    rose.set_height(10)
    rose.set_age(20)
    print("Rose updated: ", end="")
    rose.show()
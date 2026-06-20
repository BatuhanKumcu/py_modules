class Plant:
    def __init__(self, name: str, height: float, day_old: int) -> None:
        self.name = name
        self.height = height
        self.day_old = day_old

    def growth(self, growing_rate: float) -> None:
        self.height = self.height + growing_rate

    def age(self, plus_day: int=1) -> None:
        self.day_old += plus_day

    def show(self) -> None:
        print(f"{self.name}: {round(self.height,1)}cm, {self.day_old} days old")


def objects() -> None:
    plants = [
        Plant("Rose", 8.0, 5),
        Plant("Cactus", 12.2, 5),
        Plant("Sunflower", 15.5, 5),
        Plant("Fern", 0.8, 5),
        Plant("Oak", 125.0, 5),
    ]
    for plant in plants:
        print("Created: ", end="")
        plant.show()

    oak = plants[4]
    for i in range(1, 8):
        oak.growth(2.4)
        oak.age()
        i = i + 1
    print("After growing: ", end="")
    oak.show()

if __name__ == "__main__":
    print("=== Garden Recovery Output ===")
    objects()

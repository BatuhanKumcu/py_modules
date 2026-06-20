class Plant:
    increase_values = {
        "Rose": 0.8,
        "Cactus": 0.2,
        "Sunflower": 1.5,
    }

    def __init__(self, name: str, height: float, day_old: int) -> None:
        self.name = name
        self.height = height
        self.day_old = day_old

    def growth(self) -> None:
        self.height += self.increase_values[self.name]

    def age(self, plus_day: int=1) -> int:
        self.day_old += plus_day

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.day_old} days old")


def objects() -> None:
    rose = Plant("Rose", 25, 30)
    cactus = Plant("Cactus", 23, 2)
    sunflower = Plant("Sunflower", 14, 19)

    for plant in (rose, cactus, sunflower):
        start_height = plant.height
        plant.show()

        for day in range(1, 8):
            plant.growth()
            plant.age()
            print(f"=== Day {day} ===")
            plant.show()

        total_growth = plant.height - start_height
        print(f"Growth this week: {total_growth:.1f}cm")

if __name__ == "__main__":
    print("=== Garden Plant Growth ===")

    objects()

class Plant:
    def __init__(self, name: str, height_cm: float, age_days: int) -> None:
        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days

    def grow(self, amount_cm: float = 1.0) -> None:
        self.height_cm += amount_cm

    def age(self, days: int = 1) -> None:
        self.age_days += days

    def show(self) -> None:
        print(f"{self.name}: {self.height_cm:.1f}cm, {self.age_days} days old")


if __name__ == "__main__":
    plant = Plant("Rose", 25.0, 30)

    print("=== Garden Plant Growth ===")
    plant.show()

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        plant.grow(1.2)
        plant.age()
        plant.show()

    total_growth = round(plant.height_cm - 25.0, 1)
    print(f"Growth this week: {total_growth:.1f}cm")

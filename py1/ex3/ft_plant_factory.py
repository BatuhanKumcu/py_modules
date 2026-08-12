class Plant:
    def __init__(self, name: str, height_cm: float, age_days: int) -> None:
        self.name = name
        self.height_cm = float(height_cm)
        self.age_days = int(age_days)

    def grow(self, amount_cm: float = 1.0) -> None:
        self.height_cm += amount_cm

    def age(self, days: int = 1) -> None:
        self.age_days += days

    def show(self) -> None:
        print(f"{self.name}: {self.height_cm:.1f}cm, {self.age_days} days old")


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120),
    ]
    print("=== Plant Factory Output ===")
    for p in plants:
        print("Created:", end=" ")
        p.show()

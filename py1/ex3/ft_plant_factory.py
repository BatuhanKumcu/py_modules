class Plant:
	def __init__(self, name: str, height_cm: float, age_days: int) -> None:
		self.name = name
		self.height_cm = float(height_cm)
		self.age_days = int(age_days)

	def grow(self, amount_cm: float=1.0) -> None:
		self.height_cm += amount_cm

	def age(self, days: int=1) -> None:
		self.age_days += days

	def show(self, prefix: str="Created: ") -> None:
		if prefix:
			print(f"{prefix}: {self.name}: {self.height_cm:.1f}cm, {self.age_days} days old")
		else:
			print(f"{self.name}: {self.height_cm:.1f}cm, {self.age_days} days old")


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25.0, 30),
        Plant("Sunflower", 80.0, 45),
        Plant("Cactus", 15.0, 120),
        Plant("Tulip", 12.0, 10),
        Plant("Lily", 30.0, 20),
    ]
    print("=== Plant Factory Output ===")
    for p in plants:
        print("Created:", end=" ")
        p.show()

class Plant:
	def __init__(self, name, height_cm, age_days):
		self.name = name
		self.height_cm = float(height_cm)
		self.age_days = int(age_days)

	def grow(self, amount_cm=1.0):
		self.height_cm += amount_cm

	def age(self, days=1):
		self.age_days += days

	def show(self, prefix="Created: "):
		if prefix:
			print(f"{prefix}: {self.name}: {self.height_cm:.1f}cm, {self.age_days} days old")
		else:
			print(f"{self.name}: {self.height_cm:.1f}cm, {self.age_days} days old")


def main():
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

if __name__ == "__main__":
	main()
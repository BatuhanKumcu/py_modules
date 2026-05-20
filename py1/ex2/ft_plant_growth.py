class Plant:
	def __init__(self, name, height_cm, age_days):
		self.name = name
		self.height_cm = height_cm
		self.age_days = age_days

	def grow(self, amount_cm=1.0):
		self.height_cm += amount_cm

	def age(self, days=1):
		self.age_days += days

	def show(self):
		print(f"{self.name}: {self.height_cm:.1f}cm, {self.age_days} days old")


def main():
	plant = Plant("Rose", 25.0, 30)

	print("=== Garden Plant Growth ===")
	plant.show()

	for day in range(1, 8):
		print(f"=== Day {day} ===")
		plant.grow(1.2)
		plant.age()
		plant.show()

	print("=== Week Summary ===")
	total_growth = round(plant.height_cm - 25.0, 1)
	print(f"{plant.name} grew {total_growth}cm over one week.")


if __name__ == "__main__":
	main()


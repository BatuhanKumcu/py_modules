class Plant:
	def __init__(self, name, height_cm, age_days):
		self.name = name
		self.height_cm = height_cm
		self.age_days = age_days

	def show(self):
		print(f"{self.name}: {self.height_cm}cm, {self.age_days} days old")


def objects():
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    rose.show()
    sunflower.show()
    cactus.show()


if __name__ == "__main__":
    print("=== Garden Plant Registery ===")
    objects()

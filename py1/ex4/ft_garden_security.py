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

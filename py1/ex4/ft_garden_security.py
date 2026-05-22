class Plant:
	def __init__(self, name, height_cm, age_days):
		self._name = name
		self._height_cm = 0.0
		self._age_days = 0
		self.set_height(height_cm, False)
		self.set_age(age_days, False)

	def set_height(self, height_cm, display_message=True):
		if height_cm < 0:
			print(f"{self._name}: Error, height can't be negative")
			print("Height update rejected")
			return
		self._height_cm = height_cm
		if display_message:
			print(f"Height updated: {round(self._height_cm, 1)}cm")

	def set_age(self, age_days, display_message=True):
		if age_days < 0:
			print(f"{self._name}: Error, age can't be negative")
			print("Age update rejected")
			return
		self._age_days = age_days
		if display_message:
			print(f"Age updated: {self._age_days} days")

	def get_height(self):
		return self._height_cm

	def get_age(self):
		return self._age_days

	def grow(self, amount_cm=1.0):
		self.set_height(self._height_cm + amount_cm)

	def age(self, days=1):
		self.set_age(self._age_days + days)

	def show(self, prefix=""):
		if prefix:
			print(f"{prefix}: {self._name}: {self._height_cm:.1f}cm, {self._age_days} days old")
		else:
			print(f"{self._name}: {self._height_cm:.1f}cm, {self._age_days} days old")


def main():
	print("=== Garden Security System ===")
	rose = Plant("Rose", 15.0, 10)
	rose.show("Plant created")

	print()
	rose.set_height(25)
	rose.set_age(30)

	print()
	rose.set_height(-5)
	rose.set_age(-10)

	print()
	print(f"Safe height access: {rose.get_height()}cm")
	print(f"Safe age access: {rose.get_age()} days")


if __name__ == "__main__":
	main()

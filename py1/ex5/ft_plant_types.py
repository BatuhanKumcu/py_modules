class Plant:
	def __init__(self, name: str, height_cm: float, age_days: int) -> None:
		self._name = name
		self._height_cm = 0.0
		self._age_days = 0
		self.set_height(height_cm, False)
		self.set_age(age_days, False)

	def set_height(self, height_cm: float, display_message: bool=True) -> None:
		if height_cm < 0:
			print(f"{self._name}: Error, height can't be negative")
			print("Height update rejected")
			return
		self._height_cm = height_cm
		if display_message:
			print(f"Height updated: {round(self._height_cm, 1)}cm")

	def set_age(self, age_days: int, display_message: bool=True) -> None:
		if age_days < 0:
			print(f"{self._name}: Error, age can't be negative")
			print("Age update rejected")
			return
		self._age_days = age_days
		if display_message:
			print(f"Age updated: {self._age_days} days")

	def get_height(self) -> float:
		return self._height_cm

	def get_age(self) -> int:
		return self._age_days

	def grow(self, amount_cm: float=1.0) -> None:
		self.set_height(self._height_cm + amount_cm)

	def age(self, days: int=1) -> None:
		self.set_age(self._age_days + days)

	def show(self, prefix: str="") -> None:
		if prefix:
			print(f"{prefix}: {self._name}: {self._height_cm:.1f}cm, {self._age_days} days old")
		else:
			print(f"{self._name}: {self._height_cm:.1f}cm, {self._age_days} days old")

class Flower(Plant):
	def __init__(self, name: str, height_cm: float, age_days: int, color: str) -> None:
		super().__init__(name, height_cm, age_days)
		self._color = color
		self._has_bloomed = False

	def bloom(self) -> None:
		self._has_bloomed = True

	def show(self, prefix: str="") -> None:
		super().show(prefix)
		print(f"Color: {self._color}")
		if self._has_bloomed:
			print(f"{self._name} has bloomed")
		else:
			print(f"{self._name} has not bloomed yet")


class Tree(Plant):
	def __init__(self, name: str, height_cm: float, age_days: int, trunk_diameter: float) -> None:
		super().__init__(name, height_cm, age_days)
		self._trunk_diameter = trunk_diameter

	def produce_shade(self) -> None:
		print(f"{self._name} is producing shade")

	def show(self, prefix: str="") -> None:
		super().show(prefix)
		print(f"Trunk diameter: {self._trunk_diameter}cm")


class Vegetable(Plant):
	def __init__(self, name: str, height_cm: float, age_days: int, harvest_season: str):
		super().__init__(name, height_cm, age_days)
		self._harvest_season = harvest_season
		self._nutritional_value = 0

	def grow(self, amount_cm: float=1.0) -> None:
		super().grow(amount_cm)
		self._nutritional_value += 1

	def age(self, days: int=1) -> None:
		super().age(days)
		self._nutritional_value += 1

	def show(self, prefix: str="") -> None:
		super().show(prefix)
		print(f"Harvest season: {self._harvest_season}")
		print(f"Nutritional value: {self._nutritional_value}")


if __name__ == "__main__":
	print("=== Garden Plant Types ===")

	print("=== Flower")
	rose = Flower("Rose", 15.0, 10, "red")
	rose.show()
	rose.bloom()
	rose.show()

	print("\n=== Tree")
	oak = Tree("Oak", 250.0, 600, 45.0)
	oak.show()
	oak.produce_shade()

	print("\n=== Vegetable")
	carrot = Vegetable("Carrot", 8.0, 20, "April")
	carrot.show()
	carrot.grow(2.0)
	carrot.age(5)
	carrot.show()

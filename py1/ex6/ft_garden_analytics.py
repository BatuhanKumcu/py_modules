class Plant:
	class Statistics:
		def __init__(self) -> None:
			self._grow_calls = 0
			self._age_calls = 0
			self._show_calls = 0

		def add_grow(self) -> None:
			self._grow_calls += 1
		def add_age(self) -> None:
			self._age_calls += 1
		def add_show(self) -> None:
			self._show_calls += 1

		def display(self) -> None:
			print(f"Stats: {self._grow_calls} grow, {self._age_calls} age, {self._show_calls} show")

	def __init__(self, name: str, height_cm: float, age_days: int) -> None:
		self._name = name
		self._height_cm = 0.0
		self._age_days = 0
		self.set_height(height_cm, False)
		self.set_age(age_days, False)
		self._stats = self.Statistics()

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
		self._stats.add_grow()
		self.set_height(self._height_cm + amount_cm, False)

	def age(self, days: int=1) -> None:
		self._stats.add_age()
		self.set_age(self._age_days + days, False)

	def show(self, prefix: str="") -> None:
		self._stats.add_show()
		if prefix:
			print(f"{prefix}: {self._name}: {self._height_cm:.1f}cm, {self._age_days} days old")
		else:
			print(f"{self._name}: {self._height_cm:.1f}cm, {self._age_days} days old")

	def display_statistics(self) -> None:
		print(f"[statistics for {self._name}]")
		self._stats.display()

	@classmethod
	def anonymous(cls: type["Plant"]) -> "Plant":
		return cls("Unknown plant", 0.0, 0)

	@staticmethod
	def is_older_than_a_year(age_days: int) -> int:
		return age_days > 365


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
			print(f"{self._name} is blooming beautifully!")
		else:
			print(f"{self._name} has not bloomed yet")


class Tree(Plant):
	class Statistics(Plant.Statistics):
		def __init__(self) -> None:
			super().__init__()
			self._shade_calls = 0

		def add_shade(self) -> None:
			self._shade_calls += 1

		def display(self) -> None:
			super().display()
			print(f"{self._shade_calls} shade")

	def __init__(self, name: str, height_cm: float, age_days: int, trunk_diameter: float) -> None:
		super().__init__(name, height_cm, age_days)
		self._stats: Tree.Statistics = self.Statistics()
		self._trunk_diameter = trunk_diameter

	def produce_shade(self) -> None:
		self._stats.add_shade()
		print(f"Tree {self._name} now produces a shade of {self._height_cm:.1f}cm long and {self._trunk_diameter:.1f}cm wide.")

	def show(self, prefix: str="") -> None:
		super().show(prefix)
		print(f"Trunk diameter: {self._trunk_diameter:.1f}cm")


class Vegetable(Plant):
	def __init__(self, name: str, height_cm: float, age_days: int, harvest_season: str) -> None:
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


class Seed(Flower):
	def __init__(self, name: str, height_cm: float, age_days: int, color: str, seeds: int) -> None:
		super().__init__(name, height_cm, age_days, color)
		self._seeds = seeds

	def bloom(self) -> None:
		super().bloom()
		self._seeds = 42

	def show(self, prefix: str="") -> None:
		super().show(prefix)
		print(f"Seeds: {self._seeds}")


def display_statistics(plant: Plant) -> None:
	plant.display_statistics()



if __name__ == "__main__":

	print("=== Garden statistics ===")
	print("=== Check year-old")
	print(f"Is 30 days more than a year? -> {Plant.is_older_than_a_year(30)}")
	print(f"Is 400 days more than a year? -> {Plant.is_older_than_a_year(400)}")

	print("=== Flower")
	rose = Flower("Rose", 15.0, 10, "red")
	rose.show()
	display_statistics(rose)
	print("[asking the rose to grow and bloom]")
	rose.grow(8.0)
	rose.bloom()
	rose.show()
	display_statistics(rose)

	print("=== Tree")
	oak = Tree("Oak", 200.0, 365, 5.0)
	oak.show()
	display_statistics(oak)
	print("[asking the oak to produce shade]")
	oak.produce_shade()
	display_statistics(oak)

	print("=== Seed")
	sunflower = Seed("Sunflower", 80.0, 45, "yellow", 0)
	sunflower.show()
	print("[make sunflower grow, age and bloom]")
	sunflower.grow(30.0)
	sunflower.age(20)
	sunflower.bloom()
	sunflower.show()
	display_statistics(sunflower)

	print("=== Anonymous")
	unknown = Plant.anonymous()
	unknown.show()
	display_statistics(unknown)

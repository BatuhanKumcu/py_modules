class Plant:
    def __init__(self, name: str, height_cm: float, age_days: int) -> None:
        self._name = name
        self._height_cm = 0.0
        self._age_days = 0
        self.set_height(height_cm, False)
        self.set_age(age_days, False)

    def set_height(self, height_cm: float, disp_message: bool = True) -> None:
        if height_cm < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height_cm = height_cm
        if disp_message:
            print(f"Height updated: {round(self._height_cm, 1)}cm")

    def set_age(self, age_days: int, disp_message: bool = True) -> None:
        if age_days < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age_days = age_days
        if disp_message:
            print(f"Age updated: {self._age_days} days")

    def get_height(self) -> float:
        return self._height_cm

    def get_age(self) -> int:
        return self._age_days

    def grow(self, amount_cm: float = 1.0) -> None:
        self.set_height(self._height_cm + amount_cm, False)

    def age(self, days: int = 1) -> None:
        self.set_age(self._age_days + days, False)

    def show(self) -> None:
        print(
            f"{self._name}: {self._height_cm:.1f}cm, "
            f"{self._age_days} days old"
        )


class Flower(Plant):
    def __init__(
        self, name: str, height_cm: float, age_days: int, color: str
    ) -> None:
        super().__init__(name, height_cm, age_days)
        self._color = color
        self._has_bloomed = False

    def bloom(self) -> None:
        self._has_bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._has_bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(
        self, name: str, height_cm: float, age_days: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height_cm, age_days)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(
            f"Tree {self._name} now produces a shade of "
            f"{self._height_cm:.1f}cm long and "
            f"{self._trunk_diameter:.1f}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(
        self, name: str, height_cm: float, age_days: int, harvest_season: str
    ) -> None:
        super().__init__(name, height_cm, age_days)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def grow(self, amount_cm: float = 1.0) -> None:
        super().grow(amount_cm)
        self._nutritional_value += 1

    def age(self, days: int = 1) -> None:
        super().age(days)
        self._nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("\n=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")

    for _ in range(10):
        tomato.grow(4.2)
        tomato.age(2)

    tomato.show()

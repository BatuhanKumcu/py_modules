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
        self.set_height(self._height_cm + amount_cm)

    def age(self, days: int = 1) -> None:
        self.set_age(self._age_days + days)

    def show(self) -> None:
        print(
            f"{self._name}: {self._height_cm:.1f}cm, "
            f"{self._age_days} days old"
        )


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)

    print("Plant created:", end=" ")
    rose.show()

    print()
    rose.set_height(25)
    rose.set_age(30)

    print()
    rose.set_height(-5)
    rose.set_age(-10)

    print()
    print("Current state:", end=" ")
    rose.show()

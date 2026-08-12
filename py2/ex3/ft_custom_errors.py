class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)
    pass


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)
    pass


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)
    pass


def check_plant() -> None:
    raise PlantError(message="The tomato plant is wilting!")


def check_water() -> None:
    raise WaterError(message="Not enough water in the tank!")


def test_specific_errors() -> None:

    print("=== Custom Garden Errors Demo ===")
    print()

    print("Testing PlantError...")
    try:
        check_plant()
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print()
    print("Testing WaterError...")
    try:
        check_water()
    except WaterError as e:
        print(f"Caught WaterError: {e}")


def test_all_errors() -> None:
    print()
    print("Testing catching all garden errors...")

    for check in (check_plant, check_water):
        try:
            check()
        except GardenError as e:
            print(f"Caught GardenError: {e}")

    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_specific_errors()
    test_all_errors()

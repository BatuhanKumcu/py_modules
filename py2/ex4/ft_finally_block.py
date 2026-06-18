class PlantError(Exception):
    pass

def water_plant(plant_name: str) -> str:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: {plant_name}")

    print(f"Watering {plant_name}: [OK]")

def test_watering_system() -> None:
    try:
        print("Testing valid plants...")
        print("Opening watering system")
        water_plant("Lettuce")
        water_plant("Tomato")
        water_plant("Carrots")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print("... ending tests and returning to main")
    print("Closing watering system")

    try:
        print()
        print("Testing valid plants...")
        print("Opening watering system")
        water_plant("Lettuce")
        water_plant("Tomato")
        water_plant("carrots")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print("... ending tests and returning to main")
    print("Closing watering system")

if __name__ == "__main__":
    print("=== Garden Watering System ===")
    print()
    test_watering_system()

def input_temperature(temp_str: str) -> int:
    s = temp_str.strip()
    try:
        return int(s)
    except ValueError:
        raise


def test_temperature() -> None:
    data = "25"
    print(f"Input data is '{data}'")
    try:
        temp = input_temperature(data)
        print(f"Temperature is now {temp}°C")
    except ValueError as err:
        print(f"Caught input_temperature error: {err}")
    print()

    data = "abc"
    print(f"Input data is '{data}'")
    try:
        temp = input_temperature(data)
        print(f"Temperature is now {temp}°C")
    except ValueError as err:
        print(f"Caught input_temperature error: {err}")
    print()

    print("All tests completed - program didn't crash")


if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    test_temperature()

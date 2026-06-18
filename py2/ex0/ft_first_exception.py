def input_temperature(temp_str: str) -> int:
    try:
        return int(temp_str)
    except ValueError:
        raise


def test_temperature() -> None:
    data = "25"
    print(f"Input data is '{data}'")

    try:
        temp = input_temperature(data)
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print()

    data = "abc"
    print(f"Input data is '{data}'")

    try:
        temp = input_temperature(data)
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print()

    print("All tests completed - program didn't crash!")

def input_temperature(temp_str: str) -> int | None:
    temp = int(temp_str)

    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    elif temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")

    return temp


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    print()

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

    data = "-50"
    print(f"Input data is '{data}'")

    try:
        temp = input_temperature(data)
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print()

    data = "100"
    print(f"Input data is '{data}'")

    try:
        temp = input_temperature(data)
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()

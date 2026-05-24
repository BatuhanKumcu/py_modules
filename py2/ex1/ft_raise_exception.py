def input_temperature(temp_str: str):
    s = temp_str.strip()
    try:
        temp = int(s)
    except ValueError:
        raise
    
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    elif temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    
    return temp


def test_temperature():
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

    data = "100"
    print(f"Input data is '{data}'")
    try:
        temp = input_temperature(data)
        print(f"Temperature is now {temp}°C")
    except ValueError as err:
        print(f"Caught input_temperature error: {err}")
    print()

    data = "-50"
    print(f"Input data is '{data}'")
    try:
        temp = input_temperature(data)
        print(f"Temperature is now {temp}°C")
    except ValueError as err:
        print(f"Caught input_temperature error: {err}")
    print()

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    test_temperature()
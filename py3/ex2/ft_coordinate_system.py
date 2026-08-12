import math


def get_player_position() -> tuple[float, float, float]:
    position = (0.0, 0.0, 0.0)
    valid = False
    while not valid:
        user_input = input(
            "Enter new coordinates as "
            "floats in format 'x,y,z': "
        )

        parts = user_input.split(",")

        if len(parts) != 3:
            print("Invalid syntax")
            continue

        try:
            x = float(parts[0])
            y = float(parts[1])
            z = float(parts[2])
            position = (x, y, z)
            valid = True
        except ValueError:
            print("Error on parameter: ", user_input)

    return position


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print()

    print("Get a first set of coordinates")
    first_position = get_player_position()
    print("Got a first tuple: ", first_position)
    print(
        f"It includes: X={first_position[0]}, Y={first_position[1]}, "
        f"Z={first_position[2]}"
    )

    distance_to_center = math.sqrt(
        first_position[0] ** 2
        + first_position[1] ** 2
        + first_position[2] ** 2
    )
    print(f"Distance to center: {round(distance_to_center, 4)}")

    print()
    print("Get a second set of coordinates")
    second_position = get_player_position()
    print(f"Got a second tuple: {second_position}")
    distance_between = math.sqrt(
                        (second_position[0] - first_position[0]) ** 2 +
                        (second_position[1] - first_position[1]) ** 2 +
                        (second_position[2] - first_position[2]) ** 2)
    print(
        f"Distance between the 2 sets of coordinates: "
        f"{round(distance_between, 4)}"
    )

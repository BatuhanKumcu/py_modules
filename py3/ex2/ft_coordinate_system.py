import math


def get_player_pos() -> tuple[float, float, float]:
    position = (0.0, 0.0, 0.0)
    valid = False

    while not valid:
        user_input = input("Enter new coordinates as floats in format 'x,y,z': ")

        parts = user_input.split(",")

        if len(parts) != 3:
            print("Invalid syntax")
            continue

        try:
            x = float(parts[0])
            y = float(parts[1])
            z = float(parts[2])
            position = (x, y, z)
        except ValueError:
            valid = True
            print("Error on parameter:", user_input)

    return position


print("=== Game Coordinate System ===")

print("\nGet a first set of coordinates")
first_pos = get_player_pos()

print("Got a first tuple: ", first_pos)
print("It includes:", first_pos[0], first_pos[1], first_pos[2])

distance_center = math.sqrt(first_pos[0]**2 + first_pos[1]**2 + first_pos[2]**2)
print("Distance to center: ", round(distance_center, 4))

print("\nGet a second set of coordinates")
second_pos = get_player_pos()

distance_between = math.sqrt(
    (second_pos[0] - first_pos[0])**2
     + (second_pos[1] - first_pos[1])**2
    + (second_pos[2] - first_pos[2])**2
)

print("Distance between the 2 sets of coordinates:", round(distance_between, 4))

import sys

def inventory_system() -> None:
    inventory = {}

    for i in range(1, len(sys.argv)):
        parameter = sys.argv[i]

        if ":" not in parameter:
            print("Error - invalid parameter", "'" + parameter + "'")
            continue

        parts = parameter.split(":")

        if len(parts) != 2:
            print("Error - invalid parameter", "'" + parameter + "'")
            continue

        item = parts[0]
        quantity_text = (parts[1])
        try:
            quantity = int(quantity_text)
            inventory[item] = quantity
        except ValueError:
            print("Quantity error for '" + item + "': invalid literal for int() with base 10: '" + quantity_text + "'")

    print("Got inventory:", inventory)

    item_list = list(inventory.keys())
    print("Item list: ", item_list)

    total_quantity = sum(inventory.values())
    print("Total quantity of the", len(inventory), "items:", total_quantity)

    if total_quantity > 0:
        for item in inventory:
            percentage = inventory[item] / total_quantity * 100
            print("Item", item, "represent", str(round(percentage, 1)) + "%")

        most_item = item_list[0]
        least_item = item_list[0]

        for item in inventory:
            if inventory[item] > inventory[most_item]:
                most_item = item

            if inventory[item] < inventory[least_item]:
                least_item = item

        print("Item most abundant: ", most_item, "with quantity", inventory[most_item])
        print("Item least: ", least_item, "with quantity", inventory[least_item])

    inventory.update({"magic_item": 1})
    print("Updated inventory:", inventory)

print("=== Inventory System Analysis ===")
inventory_system()

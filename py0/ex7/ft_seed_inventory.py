def ft_seed_inventory(seed_type:str, amount:int, unit:str) -> None:
    seed = seed_type.capitalize()

    if unit == "packets":
        print(f"{seed} seeds: {amount} packets available")
    elif unit == "grams":
        print(f"{seed} seeds: {amount} grams total")
    elif unit == "area":
        print(f"{seed} seeds: covers {amount} square meters")
    else:
        print("Unknown unit type")

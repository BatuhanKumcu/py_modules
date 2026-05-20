def ft_plant_age():
    plantage = int(input("Enter plant age int days: "))
    if plantage < 60:
        print("Plant needs more time to grow.")
    if plantage >= 60:
        print("Plant is ready to harvest!")

def print_harvest_days(day: int, daycount: int) -> None:
    if day > daycount:
        print("Harvest time!")
        return

    print(f"Day {day}")
    print_harvest_days(day + 1, daycount)


def ft_count_harvest_recursive() -> None:
    daycount = int(input("Days until harvest: "))
    print_harvest_days(1, daycount)


if __name__ == "__main__":
    ft_count_harvest_recursive()

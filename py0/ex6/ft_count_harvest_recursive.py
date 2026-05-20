def ft_count_harvest_recursive():
    daycount = int(input("Days until harvest: "))


def rec(i):
    if i > daycount:
        return
    print(i)
    rec(i + 1)
    rec(1)
    print("Harvest time!")

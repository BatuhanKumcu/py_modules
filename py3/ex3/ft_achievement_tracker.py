import random


def gen_player_achievements():
    all_achievements = [
        "First Steps",
        "Boss Slayer",
        "Sharp Mind",
        "Treasure Hunter",
        "Speed Runner",
        "World Savior",
        "Strategist",
        "Master Explorer",
        "Crafting Genius",
        "Collector Supreme",
        "Hidden Path Finder",
        "Unstoppable",
        "Survivor",
    ]

    amount = random.randint(4, 8)
    achievements = random.sample(all_achievements, amount)

    return set(achievements)
print("=== Achievement Tracker System ===")

alice = gen_player_achievements()
bob = gen_player_achievements()
charlie = gen_player_achievements()
dylan = gen_player_achievements()

print("Player Alice:", alice)
print("Player Bob:", bob)
print("Player Charlie:", charlie)
print("Player Dylan:", dylan)

all_distinct = alice.union(bob, charlie, dylan)

print("\nAll distinct achievements:", all_distinct)

common = alice.intersection(bob, charlie, dylan)

print("\nCommon achievements:", common)

print("\nOnly Alice has: ", alice.difference(bob, charlie, dylan))
print("Only Bob has: ", bob.difference(charlie, dylan, alice))
print("Only Charlie has: ", charlie.difference(alice, dylan, bob))
print("Only Dylan has: ", dylan.difference(charlie, bob, alice))

print()
print("Alice is missing", all_distinct.difference(alice))
print("Bob is missing", all_distinct.difference(bob))
print("Charlie is missing", all_distinct.difference(charlie))
print("Dylan is missing", all_distinct.difference(dylan))

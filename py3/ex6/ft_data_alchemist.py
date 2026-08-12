import random


if __name__ == "__main__":
    print("=== Game Data Alchemist ===")

    players = [
        "Alice", "bob", "Charlie", "dylan", "Emma", "Gregory",
        "john", "kevin", "Liam"
    ]

    capital_players = [name.capitalize() for name in players]

    originally_capitalized = [name for name in players if name.istitle()]

    scores = {
        name: random.randint(0, 1000)
        for name in capital_players
    }

    average = round(sum(scores.values())/len(scores), 2)

    high_scores = {
        name: score
        for name, score in scores.items()
        if score > average
    }

    print("Initial list of players", players)
    print("New list with all names capitalized", capital_players)
    print("New list of capitalized players only", originally_capitalized)
    print("Score dict:", scores)
    print("Score average is", average)
    print("High scores:", high_scores)

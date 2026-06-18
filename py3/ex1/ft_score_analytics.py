import sys

print("=== Player Score Analytics ===")

if len(sys.argv) == 1:
    print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")

else:
    scores = []

    for i in range(1, len(sys.argv)):
        try:
            score = int(sys.argv[i])
            scores.append(score)
        except ValueError:
            print(f"Invalid parameter: {sys.argv[i]}")
        if not scores:
            print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")

    if len(scores) > 0:
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(sys.argv) - 1}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")
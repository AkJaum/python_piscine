import sys


def main():
    print("=== Player Score Analytics ===")
    if len(sys.argv) == 1:
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py "
            "<score1> <score2> ..."
        )
        return

    scores = []
    for arg in sys.argv[1:]:
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"'{arg}' -> Not a valid number")

    if not scores:
        print("No valid scores provided.")
        return

    total = sum(scores)
    count = len(scores)
    average = total / count
    high = max(scores)
    low = min(scores)
    score_range = high - low

    print(f"Scores processed: {scores}")
    print(f"Total players: {count}")
    print(f"Total score: {total}")
    print(f"Average score: {average}")
    print(f"High score: {high}")
    print(f"Low score: {low}")
    print(f"Score range: {score_range}")


main()

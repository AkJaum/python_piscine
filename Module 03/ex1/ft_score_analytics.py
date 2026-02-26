import sys


class ScoreManager():
    def __init__(self) -> None:
        self.scores = []
        self.total_players = 0
        self.total_score = 0
        self.average_score = 0

    def convert_to_list(self) -> None:
        i = 1
        while i < len(sys.argv):
            try:
                number = int(sys.argv[i])
                self.scores.append(number)
            except ValueError as Error:
                print("Error:", Error)
            i += 1

    def calculate_stats(self) -> None:
        self.total_players = len(self.scores)
        if self.total_players == 0:
            return
        self.total_score = sum(self.scores)
        self.average_score = self.total_score / self.total_players


if __name__ == "__main__":
    print("=== Player Score Analytics ===")

    if len(sys.argv) == 1:
        print(
            "No scores provided. Usage: python3",
            "ft_score_analytics.py <score1> <score2> ..."
        )
    else:
        manager = ScoreManager()
        manager.convert_to_list()
        manager.calculate_stats()

        if manager.total_players == 0:
            print("No valid scores provided.")
        else:
            print("Scores processed:", manager.scores)
            print("Total players:", manager.total_players)
            print("Total score:", manager.total_score)
            print("Average score:", manager.average_score)
            print("High score:", max(manager.scores))
            print("Low score:", min(manager.scores))
            print("Score range:", max(manager.scores) - min(manager.scores))

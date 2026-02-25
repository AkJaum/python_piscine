def main():
    print("=== Game Analytics Dashboard ===")
    players = [
        {
            "name": "alice",
            "score": 2300,
            "achievements": ["first_kill", "level_10", "boss_slayer"],
            "active": True,
            "region": "north"
        },
        {
            "name": "bob",
            "score": 1800,
            "achievements": ["first_kill", "level_10"],
            "active": True,
            "region": "east"
        },
        {
            "name": "charlie",
            "score": 2150,
            "achievements": ["boss_slayer", "treasure_hunter"],
            "active": True,
            "region": "central"
        },
        {
            "name": "diana",
            "score": 2050,
            "achievements": ["first_kill"],
            "active": False,
            "region": "north"
        }
    ]
    print("\n=== List Comprehension Examples ===")
    high_scorers = [p["name"] for p in players if p["score"] > 2000]
    print("High scorers (>2000):", high_scorers)
    scores_doubled = [p["score"] * 2 for p in players]
    print("Scores doubled:", scores_doubled)
    active_players = [p["name"] for p in players if p["active"]]
    print("Active players:", active_players)
    print("\n=== Dict Comprehension Examples ===")
    player_scores = {p["name"]: p["score"] for p in players}
    print("Player scores:", player_scores)
    score_categories = {
        "high": len([p for p in players if p["score"] > 2000]),
        "medium": len([p for p in players if 1500 <= p["score"] <= 2000]),
        "low": len([p for p in players if p["score"] < 1500])
    }
    print("Score categories:", score_categories)
    achievement_counts = {
        p["name"]: len(p["achievements"])
        for p in players
    }
    print("Achievement counts:", achievement_counts)
    print("\n=== Set Comprehension Examples ===")
    unique_players = {p["name"] for p in players}
    print("Unique players:", unique_players)
    unique_achievements = {
        achievement
        for p in players
        for achievement in p["achievements"]
    }
    print("Unique achievements:", unique_achievements)
    unique_regions = {p["region"] for p in players}
    print("Active regions:", unique_regions)
    print("\n=== Combined Analysis ===")
    total_players = len(players)
    print("Total players:", total_players)
    total_unique_achievements = sum([len(p["achievements"]) for p in players])
    print("Total unique achievements:", total_unique_achievements)
    average_score = sum([p["score"] for p in players]) / len(players)
    print("Average score:", average_score)
    top_player = max(players, key=lambda p: p["score"])
    print("Top performer:",
          top_player["name"],
          f"({top_player['score']} points, {len(top_player['achievements'])} achievements)")

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    alice = set(["first_kill", "level_10", "treasure_hunter", "speed_demon"])
    bob = set(["first_kill", "level_10", "boss_slayer", "collector"])
    charlie = set(
        [
            "level_10", "treasure_hunter", "boss_slayer",
            "speed_demon", "perfectionist"
        ]
    )
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")
    print("\n=== Achievement Analytics ===")
    all_achievements = alice.union(bob).union(charlie)
    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements {len(all_achievements)}\n")
    common_all = alice.intersection(bob).intersection(charlie)
    print(f"Common to all players: {common_all}")
    rare_achievements = (
        (alice - bob - charlie)
        | (bob - alice - charlie)
        | (charlie - alice - bob)
    )
    print(f"Rare achievements (1 player): {rare_achievements}\n")
    print(f"Alice vc Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")

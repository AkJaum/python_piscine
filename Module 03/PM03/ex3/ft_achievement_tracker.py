def main():
    print("=== Achievement Tracker System ===\n")
    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasure_hunter',
               'boss_slayer', 'speed_demon', 'perfectionist'}
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")
    print("\n=== Achievement Analytics ===")
    u_achievement = alice.union(bob).union(charlie)
    print(f"All unique achievements: {u_achievement}")
    print(f"Total unique achievements: {len(u_achievement)}\n")
    c_achievement = alice.intersection(bob).intersection(charlie)
    r_achievement = set()
    for a in u_achievement:
        count = (a in alice) + (a in bob) + (a in charlie)
        if count == 1:
            r_achievement = r_achievement.union({a})
    """ Its possible to do it like the bellow too.
    u_achievement = (alice.difference(bob).difference(charlie)
    ).union(bob.difference(alice).difference(charlie)
    ).union(charlie.difference(alice).difference(bob))"""
    print(f"Common to all players: {c_achievement}")
    print(f"Rare achievements (1 player): {r_achievement}\n")
    print(f"Alice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")


# Allowed functions (brief notes):
# - set(): create a set from an iterable or use a literal {a, b}.
#   Useful to store unique achievements and remove duplicates.
# - union(): setA.union(setB) returns a set with elements in either set.
#   Use union to combine achievements from multiple players.
# - intersection(): setA.intersection(setB) returns items common to both.
#   Chain intersections to find achievements shared by many players.
# - difference(): setA.difference(setB) returns items in A not in B.
#   Useful to find what one player has that another does not.

main()

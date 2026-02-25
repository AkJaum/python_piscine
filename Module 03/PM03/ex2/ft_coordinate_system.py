import sys
import math


# it's an euclidean formula(**2 look like power 2)
def distance(p1: list, p2: list):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    dz = p2[2] - p1[2]
    return math.sqrt(dx**2 + dy**2 + dz**2)


def parse_coord_string(s):
    parts = s.split(",")
    if len(parts) != 3:
        return None, ValueError("Expected 3 components")
    try:
        x = int(parts[0])
        y = int(parts[1])
        z = int(parts[2])
    except ValueError as e:
        return None, e
    return (x, y, z), None


def main():
    print("=== Game Coordinate System ===\n")
    spawn = (0, 0, 0)
    town = (520, 720, 200)
    boss = (200, 350, 157)

    # No args -> default to spawn (0,0,0)
    if len(sys.argv) == 1:
        position = (0, 0, 0)
    # One arg like "x,y,z" (accepts "5,4,3" and "5, 4, 3")
    elif len(sys.argv) == 2:
        s = sys.argv[1]
        print(f'Parsing coordinates: "{s}"')
        pos, err = parse_coord_string(s)
        if err is not None:
            print(f"Error parsing coordinates: {err}")
            print(f"Error details - Args: {err.args}")
            return
        position = pos
        print(f"Parsed position: {position}")
    # Three separate args: x y z
    elif len(sys.argv) == 4:
        try:
            position = (int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
        except ValueError as e:
            print(f"Error parsing coordinates: {e}")
            print(f"Error details - Args: {e.args}")
            return
    else:
        print("Provide none, one 'x,y,z' or three args x y z")
        return

    print(f"Your position: {position}")
    print(f"Spawn position: {spawn}")
    print(f"Town position: {town}")
    print(f"Boss position: {boss}\n")
    print(f"Distance between you and spawn: {distance(position, spawn):.2f}")
    print(f"Distance between you and town: {distance(position, town):.2f}")
    print(f"Distance between you and boss: {distance(position, boss):.2f}")

    print("\nUnpacking demonstration:")
    # Unpacking: variables receive the elements of the tuple in the same order.
    # Example: position = (3, 4, 0) -> x=3, y=4, z=0
    # To ignore a component use underscore: x, _, z = position
    x, y, z = position
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


main()
""" its possible to use tupple in some ways, but here i used as
literal tupple, for example: (1 5 3)
to use the function, i would have to give an already made list, for example:
lst = [5, 2, 3]
tupple_list = tuple(lst)
of course, we can use it in more than just this 2 ways, but its only a resume
its look like that tuple is a bit more light than a list and it can evade bugs
since a tupple can't be changed.
Beside here we are limited, usually a tuple would be use to places since it
mostly wouldn't be changed of their place, while a player would be better with
a list since he would normally move to a place to another.

i analyzed the exercize and, by my judge, it give us two ways to do it
one of them is like i did, using argv since its allowed there, but the other
way is to use a pre-made list that we would convert it to tupple"""

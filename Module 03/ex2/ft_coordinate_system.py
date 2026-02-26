import math


def parse_coords(coord_str: str) -> tuple:
    coords = coord_str.split(",")
    try:
        x = int(coords[0])
        y = int(coords[1])
        z = int(coords[2])
        pos = (x, y, z)
        return pos
    except ValueError as Error:
        print("Error parsing coordinates:", Error)
        print(
            f"Error details - Type: {type(Error).__name__}, "
            f"Args: {Error.args}\n"
        )
    return None


def create_pos(x: int, y: int, z: int) -> tuple:
    pos = (x, y, z)
    print("Position created:", pos)
    return pos


def calculate_distance(src: tuple, dest: tuple) -> float:
    x1, y1, z1 = src
    x2, y2, z2 = dest
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    print(f"Distance between {src} and {dest}: {distance:.2f}\n")


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    origin = (0, 0, 0)
    player = create_pos(10, 20, 5)
    calculate_distance(origin, player)
    coord_str = "3,4,0"
    print(f'Parsing coordinates: "{coord_str}"')
    coord = parse_coords(coord_str)
    print(f"Parsed position: {coord}")
    if coord is not None:
        calculate_distance(origin, coord)
    print('Parsing invalid coordniates: "abc,def,ghi"')
    parse_coords("abc,def,ghi")
    print("Unpacking demonstration:")
    x, y, z = coord
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")

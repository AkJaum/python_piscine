from alchemy.elements import create_air


def main() -> str:
    return create_air()


if __name__ == "__main__":
    print('=== Alembic 3 ===')
    print("Using: 'from ... import ...' structure to acess elements.py")
    print(f"Testing create_air: {main()}")

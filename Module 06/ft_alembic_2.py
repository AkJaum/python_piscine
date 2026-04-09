from alchemy.elements import create_earth


def main() -> str:
    return create_earth()


if __name__ == "__main__":
    print('=== Alembic 2 ===')
    print("Using: '... import ...' structure to acess elements.py")
    print(f"Testing create_earth: {main()}")

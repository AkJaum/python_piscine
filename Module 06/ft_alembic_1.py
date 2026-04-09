from elements import create_water


def main() -> str:
    return create_water()


if __name__ == "__main__":
    print('=== Alembic 1 ===')
    print("Using: '... import ...' structure to acess elements.py")
    print(f"Testing create_water: {main()}")

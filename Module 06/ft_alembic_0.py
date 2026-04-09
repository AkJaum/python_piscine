import elements


def main() -> str:
    return elements.create_fire()


if __name__ == "__main__":
    print('=== Alembic 0 ===')
    print("Using: 'import ...' structure to acess elements.py")
    print(f"Testing create_fire: {main()}")

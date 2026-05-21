from typing import Callable


def mage_counter() -> Callable:
    nonlocal_count = 0

    def count_mages() -> int:
        nonlocal nonlocal_count
        nonlocal_count += 1
        return nonlocal_count

    return count_mages


def spell_accumulator(initial_power: int) -> Callable:
    current_power = initial_power

    def accumulate_spell(power: int) -> int:
        nonlocal current_power
        current_power += power
        return current_power

    return accumulate_spell


def enchantment_factory(enchantment_type: str) -> Callable:
    def create_enchantment(item: str) -> str:
        return f"{enchantment_type} {item}"
    return create_enchantment


def memory_vault() -> dict[str, Callable]:
    vault = {}

    def store(key, value):
        vault[key] = value

    def recall(key):
        return vault.get(key, "Memory not found")

    return {'store': store, 'recall': recall}


if __name__ == "__main__":
    print("Testing mage counter...")
    counter_a = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    counter_b = mage_counter()
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    accumulator = spell_accumulator(100)
    print(f"Base 100, add 20: {accumulator(20)}")
    print(f"Base 100, add 30: {accumulator(30)}")

    print("\nTesting enchantment factory...")
    fire_enchantment = enchantment_factory("Flaming")
    ice_enchantment = enchantment_factory("Frozen")
    print(fire_enchantment("Sword"))
    print(ice_enchantment("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()
    print("Store 'secret' = 42")
    vault['store']('secret', 42)
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")
